import streamlit as st
from src.utils.loader import load_md

def render_publications():
    st.markdown(load_md("publications/publications.md"))