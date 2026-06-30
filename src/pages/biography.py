import streamlit as st
from src.utils.loader import load_md

def render_biography():
    st.markdown(load_md("biography/faculty_bio.md"))
    st.markdown(load_md("biography/executive_summary.md"))