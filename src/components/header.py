import streamlit as st

from src.config import APP_AUTHOR, APP_TAGLINE

def render_header():
    st.title(APP_AUTHOR)
    st.caption(APP_TAGLINE)