import streamlit as st

PAGES = [
    "Home",
    "Biography",
    "Research Program",
    "Publications",
    "Software",
    "Teaching",
    "Collaborations",
    "Research Atlas",
    "Timeline",
]

def render_sidebar():
    st.sidebar.title("Research Portfolio")
    return st.sidebar.radio("Navigate", PAGES)