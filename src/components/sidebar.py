import streamlit as st

PAGES = [
    "Home",
    "Biography",
    "Research Program",
    "Publications",
    "Software",
    "Teaching",
    "Collaborations",
    "Timeline",
]

def render_sidebar():
    st.sidebar.title("Research Portfolio")
    return st.sidebar.radio("Navigate", PAGES)