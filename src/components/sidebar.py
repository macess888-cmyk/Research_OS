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
    "Admin Editor",
    "Build Center",
]

def render_sidebar():
    st.sidebar.title("Research Portfolio")
    return st.sidebar.radio("Navigate", PAGES)