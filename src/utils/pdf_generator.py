from pathlib import Path
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch

ROOT = Path(__file__).resolve().parents[2]
CONTENT = ROOT / "content"
OUTPUT = ROOT / "output"

SECTIONS = [
    ("Biography", "biography/faculty_bio.md"),
    ("Executive Summary", "biography/executive_summary.md"),
    ("Research Program", "research/research_program.md"),
    ("Publications", "publications/publications.md"),
    ("Teaching Statement", "teaching/teaching_statement.md"),
    ("Collaborations", "collaborations/collaborations.md"),
    ("Timeline", "timeline/timeline.md"),
]

def clean_markdown(text: str) -> str:
    return (
        text.replace("# ", "")
        .replace("## ", "")
        .replace("### ", "")
        .replace("**", "")
        .replace("↓", "->")
        .replace("│", "|")
        .replace("├──", "-")
        .replace("└──", "-")
    )

def generate_faculty_dossier():
    OUTPUT.mkdir(exist_ok=True)

    out_path = OUTPUT / "Jake_Macdonald_Faculty_Dossier.pdf"
    doc = SimpleDocTemplate(str(out_path))

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("Jake Macdonald", styles["Title"]))
    story.append(Paragraph("Faculty Dossier & Academic Research Portfolio", styles["Heading2"]))
    story.append(Paragraph("Hybrid Systems Architect • Founder, HACR Hybrid Observatory", styles["BodyText"]))
    story.append(Spacer(1, 0.25 * inch))

    story.append(Paragraph("Research Profiles", styles["Heading1"]))
    story.append(Paragraph("Email: 00jake@orocore.one", styles["BodyText"]))
    story.append(Paragraph("LinkedIn: https://linkedin.com/in/jake-macdonald-45394a393", styles["BodyText"]))
    story.append(Paragraph("ORCID: https://orcid.org/0009-0000-6513-7049", styles["BodyText"]))
    story.append(Paragraph("GitHub: https://github.com/macess888-cmyk/HACR_Hybrid_Observatory", styles["BodyText"]))
    story.append(Spacer(1, 0.2 * inch))

    for title, rel_path in SECTIONS:
        path = CONTENT / rel_path
        if path.exists():
            text = clean_markdown(path.read_text(encoding="utf-8"))
            story.append(Paragraph(title, styles["Heading1"]))
            for para in text.split("\n\n"):
                if para.strip():
                    story.append(Paragraph(para.strip().replace("\n", "<br/>"), styles["BodyText"]))
                    story.append(Spacer(1, 0.08 * inch))

    doc.build(story)
    return out_path