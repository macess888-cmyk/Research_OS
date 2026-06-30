import streamlit as st
from src.utils.loader import load_md

def render_teaching():
    st.markdown(load_md("teaching/teaching_statement.md"))