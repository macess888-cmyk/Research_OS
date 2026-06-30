import streamlit as st
from src.utils.loader import load_md

def render_software():
    st.markdown(load_md("software/hacr.md"))