import streamlit as st
from pathlib import Path
from datetime import datetime
import shutil

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "output"
CONTENT = ROOT / "content"

def render_build_center():
    st.header("Build Center")
    st.caption("Generate exports, backups, and future dossier outputs.")

    OUTPUT.mkdir(exist_ok=True)

    st.subheader("Available Builds")

    if st.button("Create Portfolio Backup"):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = OUTPUT / f"portfolio_backup_{timestamp}"
        shutil.make_archive(str(backup_name), "zip", CONTENT)
        st.success(f"Backup created: {backup_name}.zip")

    if st.button("Generate Faculty Dossier"):
        placeholder = OUTPUT / "Jake_Macdonald_Faculty_Dossier_PLACEHOLDER.txt"
        placeholder.write_text(
            "Faculty dossier generation placeholder.\nPDF builder will be added in v0.9.\n",
            encoding="utf-8"
        )
        st.success("Faculty dossier placeholder created.")

    if st.button("Generate Academic CV"):
        placeholder = OUTPUT / "Jake_Macdonald_Academic_CV_PLACEHOLDER.txt"
        placeholder.write_text(
            "Academic CV generation placeholder.\nCV builder will be added in v0.9.\n",
            encoding="utf-8"
        )
        st.success("Academic CV placeholder created.")

    st.subheader("Output Folder")
    files = list(OUTPUT.glob("*"))
    if files:
        for file in files:
            st.write(file.name)
    else:
        st.write("No output files yet.")