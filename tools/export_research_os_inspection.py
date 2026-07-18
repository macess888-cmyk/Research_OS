from __future__ import annotations

import ast
import subprocess
from datetime import datetime
from pathlib import Path


EXCLUDED_DIRS = {
    ".git",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".venv",
    "venv",
    "env",
    "inspection_exports",
}


def run_git(repository_root: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repository_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        shell=False,
        timeout=15,
        check=False,
    )

    if result.returncode != 0:
        return f"UNAVAILABLE: {result.stderr.strip()}"

    return result.stdout.strip()


def relative_path(path: Path, repository_root: Path) -> str:
    return path.relative_to(repository_root).as_posix()


def collect_files(
    repository_root: Path,
    relative_directory: str,
    extension: str | None = None,
) -> list[Path]:
    root = repository_root / relative_directory

    if not root.exists():
        return []

    files: list[Path] = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue

        if any(part in EXCLUDED_DIRS for part in path.parts):
            continue

        if extension is not None and path.suffix != extension:
            continue

        files.append(path)

    return sorted(
        files,
        key=lambda item: relative_path(item, repository_root),
    )


def format_annotation(node: ast.expr | None) -> str:
    if node is None:
        return ""

    try:
        return ast.unparse(node)
    except Exception:
        return "<unavailable>"


def format_function_signature(
    node: ast.FunctionDef | ast.AsyncFunctionDef,
) -> str:
    parameters: list[str] = []

    positional = [*node.args.posonlyargs, *node.args.args]
    defaults_offset = len(positional) - len(node.args.defaults)

    for index, argument in enumerate(positional):
        value = argument.arg

        annotation = format_annotation(argument.annotation)
        if annotation:
            value += f": {annotation}"

        if index >= defaults_offset:
            value += " = ..."

        parameters.append(value)

    if node.args.vararg is not None:
        value = f"*{node.args.vararg.arg}"
        annotation = format_annotation(node.args.vararg.annotation)
        if annotation:
            value += f": {annotation}"
        parameters.append(value)
    elif node.args.kwonlyargs:
        parameters.append("*")

    for argument, default in zip(
        node.args.kwonlyargs,
        node.args.kw_defaults,
    ):
        value = argument.arg

        annotation = format_annotation(argument.annotation)
        if annotation:
            value += f": {annotation}"

        if default is not None:
            value += " = ..."

        parameters.append(value)

    if node.args.kwarg is not None:
        value = f"**{node.args.kwarg.arg}"
        annotation = format_annotation(node.args.kwarg.annotation)
        if annotation:
            value += f": {annotation}"
        parameters.append(value)

    prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
    signature = f"{prefix} {node.name}({', '.join(parameters)})"

    return_annotation = format_annotation(node.returns)
    if return_annotation:
        signature += f" -> {return_annotation}"

    return signature


def inspect_python_file(path: Path) -> tuple[list[str], list[str]]:
    source = path.read_text(
        encoding="utf-8",
        errors="strict",
    )
    tree = ast.parse(source, filename=str(path))

    classes: list[str] = []
    functions: list[str] = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef) and not node.name.startswith("_"):
            classes.append(f"class {node.name}")

            for child in node.body:
                if not isinstance(
                    child,
                    (ast.FunctionDef, ast.AsyncFunctionDef),
                ):
                    continue

                if child.name.startswith("_") and child.name != "__init__":
                    continue

                classes.append(
                    f"  - {format_function_signature(child)}"
                )

        elif isinstance(
            node,
            (ast.FunctionDef, ast.AsyncFunctionDef),
        ) and not node.name.startswith("_"):
            functions.append(format_function_signature(node))

    return classes, functions


def append_file_inventory(
    lines: list[str],
    heading: str,
    files: list[Path],
    repository_root: Path,
) -> None:
    lines.extend(
        [
            f"## {heading}",
            "",
            "| Path | Bytes |",
            "|---|---:|",
        ]
    )

    if not files:
        lines.append("| _None observed_ | 0 |")
    else:
        for path in files:
            lines.append(
                f"| `{relative_path(path, repository_root)}` "
                f"| {path.stat().st_size} |"
            )

    lines.append("")


def append_python_inventory(
    lines: list[str],
    heading: str,
    files: list[Path],
    repository_root: Path,
) -> None:
    lines.extend([f"## {heading}", ""])

    if not files:
        lines.extend(["_None observed._", ""])
        return

    for path in files:
        lines.append(
            f"### `{relative_path(path, repository_root)}`"
        )
        lines.append("")

        try:
            classes, functions = inspect_python_file(path)

            if classes:
                lines.append("Classes and methods:")
                lines.append("```text")
                lines.extend(classes)
                lines.append("```")

            if functions:
                lines.append("Functions:")
                lines.append("```text")
                lines.extend(functions)
                lines.append("```")

            if not classes and not functions:
                lines.append("_No public symbols observed._")

        except (OSError, UnicodeError, SyntaxError) as error:
            lines.append(
                f"_Inspection warning: {type(error).__name__}_"
            )

        lines.append("")


def build_package(repository_root: Path) -> str:
    generation_time = datetime.now().astimezone()
    timestamp_text = generation_time.isoformat(timespec="seconds")

    branch = run_git(
        repository_root,
        "branch",
        "--show-current",
    )
    head = run_git(
        repository_root,
        "rev-parse",
        "HEAD",
    )
    status = run_git(
        repository_root,
        "status",
        "--porcelain=v1",
        "--branch",
    )
    commits = run_git(
        repository_root,
        "log",
        "-5",
        "--pretty=format:%h\t%s",
    )

    top_level_files = sorted(
        [
            path
            for path in repository_root.iterdir()
            if path.is_file()
        ],
        key=lambda item: item.name,
    )

    model_files = collect_files(
        repository_root,
        "models",
        ".py",
    )
    service_files = collect_files(
        repository_root,
        "services",
        ".py",
    )
    test_files = collect_files(
        repository_root,
        "tests",
        ".py",
    )
    runtime_docs = collect_files(
        repository_root,
        "docs/runtime_kernel",
    )

    lines: list[str] = [
        "# RESEARCH OS — READ-ONLY INSPECTION PACKAGE",
        "",
        "## Package Metadata",
        "",
        "- Package Schema Version: `1.0`",
        "- Generator Version: `1.0.0`",
        f"- Generation Time: `{timestamp_text}`",
        f"- Repository Name: `{repository_root.name}`",
        f"- HEAD Commit: `{head}`",
        "- Inspection Posture: `OBSERVED / NON-CERTIFYING`",
        "",
        "## Inspection Scope",
        "",
        "Included:",
        "",
        "- Repository root files",
        "- Git branch, HEAD, status, and five recent commits",
        "- `models/**/*.py`",
        "- `services/**/*.py`",
        "- `tests/**/*.py`",
        "- `docs/runtime_kernel/*`",
        "- Static Python symbol inspection",
        "",
        "Excluded:",
        "",
        "- Full source contents",
        "- Test execution",
        "- Environment variables and credentials",
        "- Remote URLs",
        "- Network transmission",
        "- Certification, admission, trust, and authority",
        "",
        "## Repository State",
        "",
        f"- Current Branch: `{branch}`",
        f"- HEAD Commit: `{head}`",
        "",
        "### Git Status",
        "",
        "```text",
        status or "WORKING TREE CLEAN",
        "```",
        "",
        "## Recent Commits",
        "",
        "```text",
        commits or "UNAVAILABLE",
        "```",
        "",
    ]

    append_file_inventory(
        lines,
        "Top-Level Files",
        top_level_files,
        repository_root,
    )
    append_python_inventory(
        lines,
        "Models",
        model_files,
        repository_root,
    )
    append_python_inventory(
        lines,
        "Services",
        service_files,
        repository_root,
    )

    lines.extend(["## Tests", ""])

    for path in test_files:
        try:
            source = path.read_text(
                encoding="utf-8",
                errors="strict",
            )
            tree = ast.parse(source, filename=str(path))

            test_count = sum(
                1
                for node in tree.body
                if isinstance(
                    node,
                    (ast.FunctionDef, ast.AsyncFunctionDef),
                )
                and node.name.startswith("test_")
            )

            lines.append(
                f"- `{relative_path(path, repository_root)}` "
                f"— {test_count} top-level tests"
            )
        except (OSError, UnicodeError, SyntaxError) as error:
            lines.append(
                f"- `{relative_path(path, repository_root)}` "
                f"— warning: {type(error).__name__}"
            )

    if not test_files:
        lines.append("_None observed._")

    lines.extend(
        [
            "",
            "Test Execution: `NOT PERFORMED`",
            "",
        ]
    )

    append_file_inventory(
        lines,
        "Runtime-Kernel Documents",
        runtime_docs,
        repository_root,
    )

    lines.extend(
        [
            "## Inspection Limitations",
            "",
            "- Current accessible repository state only",
            "- Local Git metadata only",
            "- No independent remote verification",
            "- Selected directories only",
            "- Static source parsing only",
            "- No semantic document review",
            "- No test execution",
            "- Repository state was not locked during inspection",
            "",
            "## Unknown Register",
            "",
            "- Repository state may change during generation",
            "- Excluded files and directories were not inspected",
            "- Remote repository state was not independently verified",
            "",
            "## Manual Transfer Boundary",
            "",
            "This package was written locally.",
            "",
            "No network transmission was performed.",
            "",
            "Any sharing or upload requires a separate human action.",
            "",
            "## Final Status",
            "",
            "```text",
            "Repository State: OBSERVED",
            "Git State: OBSERVED",
            "File Inventory: OBSERVED",
            "Source Signatures: OBSERVED",
            "Tests: NOT EXECUTED",
            "Package Persistence: LOCAL FILE",
            "Transmission: NOT PERFORMED",
            "Certification: NONE",
            "Admission: NONE",
            "Trust: NONE",
            "Authority: NONE",
            "UNKNOWN → HOLD",
            "```",
            "",
        ]
    )

    return "\n".join(lines)


def export_package(repository_root: Path) -> Path:
    repository_root = repository_root.resolve()

    if not repository_root.exists():
        raise FileNotFoundError(
            f"repository root does not exist: {repository_root}"
        )

    if not repository_root.is_dir():
        raise NotADirectoryError(
            f"repository root is not a directory: {repository_root}"
        )

    git_check = run_git(
        repository_root,
        "rev-parse",
        "--is-inside-work-tree",
    )

    if git_check != "true":
        raise RuntimeError(
            "repository root must contain a Git working tree"
        )

    output_directory = repository_root / "inspection_exports"
    output_directory.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = (
        output_directory
        / f"research_os_inspection_{timestamp}.md"
    )

    if output_path.exists():
        raise FileExistsError(
            f"inspection package already exists: {output_path.name}"
        )

    package_text = build_package(repository_root)
    temporary_path = output_path.with_suffix(".tmp")

    try:
        temporary_path.write_text(
            package_text,
            encoding="utf-8",
            newline="\n",
        )
        temporary_path.replace(output_path)
    finally:
        if temporary_path.exists():
            temporary_path.unlink()

    return output_path


def main() -> int:
    repository_root = Path.cwd()

    try:
        output_path = export_package(repository_root)
    except Exception as error:
        print(
            f"Inspection export failed: "
            f"{type(error).__name__}: {error}"
        )
        return 1

    print(f"Inspection package created: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())