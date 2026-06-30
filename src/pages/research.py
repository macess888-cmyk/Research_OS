import streamlit as st
from src.utils.loader import load_md

def render_research():
    st.markdown(load_md("research/research_program.md"))