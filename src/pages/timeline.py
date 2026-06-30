import streamlit as st
from src.utils.loader import load_md

def render_timeline():
    st.markdown(load_md("timeline/timeline.md"))