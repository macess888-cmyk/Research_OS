import streamlit as st
from src.utils.loader import load_md

def render_collaborations():
    st.markdown(load_md("collaborations/collaborations.md"))