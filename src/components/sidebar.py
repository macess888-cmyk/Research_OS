import streamlit as st

PAGES = [
    "Dashboard",
    "Biography",
    "Research Program",
    "Publications",
    "Software",
    "Teaching",
    "Collaborations",
    "Research Atlas",
    "Timeline",
    "Search",
    "Admin Editor",
    "Build Center",
    "Knowledge Graph",
]

def render_sidebar():
    st.sidebar.title("Research OS")
    st.sidebar.caption("v1.0.0")

    st.sidebar.markdown("---")
    page = st.sidebar.radio("Navigate", PAGES)

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Jake Macdonald**")
    st.sidebar.caption("Hybrid Systems Architect")
    st.sidebar.caption("Kelowna, BC, Canada")

    return page