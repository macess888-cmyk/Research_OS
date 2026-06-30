from pathlib import Path

ROOT = Path(__file__).parent

files = {
    "README.md": "# Jake Macdonald Academic Portfolio\n\nAcademic portfolio source repository.\n",
    "ROADMAP.md": "# Roadmap\n\n- Build dossier\n- Add software pages\n- Add teaching package\n- Add GitHub Pages site\n",
    "biography/faculty_bio.md": "# Faculty Biography\n\nJake Macdonald is a Hybrid Systems Architect and founder of the HACR Hybrid Observatory.\n",
    "biography/executive_summary.md": "# Executive Summary\n\nIndependent researcher focused on AI governance, observability, resilience engineering, and boundary-based systems.\n",
    "cv/contact.md": "# Contact\n\nJake Macdonald\nKelowna, British Columbia, Canada\n00jake@orocore.one\n",
    "publications/orcid.md": "# ORCID\n\nhttps://orcid.org/0009-0000-6513-7049\n",
    "software/hacr.md": "# HACR Hybrid Observatory\n\nhttps://github.com/macess888-cmyk/HACR_Hybrid_Observatory\n",
    "teaching/teaching_statement.md": "# Teaching Statement\n\nTeaching emphasizes evidence, systems reasoning, uncertainty, and careful distinction between observation and authority.\n",
}

for path, content in files.items():
    full_path = ROOT / path
    full_path.parent.mkdir(parents=True, exist_ok=True)
    full_path.write_text(content, encoding="utf-8")

print("Academic portfolio files created.")