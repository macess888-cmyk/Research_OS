import streamlit as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"

FILES = {
    "Faculty Bio": "biography/faculty_bio.md",
    "Executive Summary": "biography/executive_summary.md",
    "Research Program": "research/research_program.md",
    "Publications": "publications/publications.md",
    "Software - HACR": "software/hacr.md",
    "Teaching Statement": "teaching/teaching_statement.md",
    "Collaborations": "collaborations/collaborations.md",
    "Timeline": "timeline/timeline.md",
}

def render_admin():
    st.header("Admin Editor")
    st.caption("Edit portfolio Markdown files directly from the app.")

    selected = st.selectbox("Choose file", list(FILES.keys()))
    file_path = CONTENT / FILES[selected]

    if not file_path.exists():
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text("", encoding="utf-8")

    current = file_path.read_text(encoding="utf-8")

    updated = st.text_area(
        "Markdown content",
        value=current,
        height=450
    )

    if st.button("Save"):
        file_path.write_text(updated, encoding="utf-8")
        st.success(f"Saved {FILES[selected]}")