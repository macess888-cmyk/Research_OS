import streamlit as st
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOCTRINE = ROOT / "docs" / "DESIGN_DOCTRINE.md"


def render_doctrine():
    st.title("Design Doctrine")

    if DOCTRINE.exists():
        st.markdown(DOCTRINE.read_text(encoding="utf-8"))
    else:
        st.warning("DESIGN_DOCTRINE.md not found.")