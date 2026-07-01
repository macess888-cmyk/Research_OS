import streamlit as st
from pathlib import Path
from datetime import datetime
import shutil

from src.utils.pdf_generator import generate_faculty_dossier
from src.services.event_engine import EventEngine

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output"
CONTENT = ROOT / "content"


def render_build_center():
    st.header("Build Center")
    st.caption("Generate exports, backups, and dossier outputs.")

    OUTPUT.mkdir(exist_ok=True)

    events = EventEngine()

    st.subheader("PDF Exports")

    if st.button("Generate Faculty Dossier"):
        pdf_path = generate_faculty_dossier()

        events.publish(
            category="Build Center",
            action=f"Faculty dossier generated: {pdf_path.name}",
            status="SUCCESS",
        )

        st.success(f"Faculty dossier created: {pdf_path.name}")

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="Download Faculty Dossier",
                data=f,
                file_name=pdf_path.name,
                mime="application/pdf",
            )

    st.subheader("Backups")

    if st.button("Create Portfolio Backup"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_base = OUTPUT / f"portfolio_backup_{timestamp}"
        backup_zip = shutil.make_archive(str(backup_base), "zip", CONTENT)

        events.publish(
            category="Build Center",
            action=f"Backup created: {Path(backup_zip).name}",
            status="SUCCESS",
        )

        st.success(f"Backup created: {Path(backup_zip).name}")

        with open(backup_zip, "rb") as f:
            st.download_button(
                label="Download Backup ZIP",
                data=f,
                file_name=Path(backup_zip).name,
                mime="application/zip",
            )

    st.subheader("Output Folder")

    files = sorted(OUTPUT.glob("*"))

    if files:
        for file in files:
            st.write(file.name)
    else:
        st.write("No output files yet.")