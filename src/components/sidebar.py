import streamlit as st

from src.config import APP_NAME, APP_VERSION, APP_AUTHOR, APP_TAGLINE, APP_LOCATION

PAGES = [
    "Dashboard",
    "System Health",

    "Biography",
    "About",
    "Research Program",
    "Publications",
    "Teaching",
    "Collaborations",

    "Software",
    "Repositories",
    "Research Workspace",

    "Research Atlas",
    "Knowledge Graph",
    "Research Registry",
    "Timeline",
    "Search",
    "Validation",

    "Admin Editor",
    "Build Center",
]

def render_sidebar():
    st.sidebar.title(APP_NAME)
    st.sidebar.caption(APP_VERSION)

    st.sidebar.markdown("---")
    page = st.sidebar.radio("Navigate", PAGES)

    st.sidebar.markdown("---")
    st.sidebar.markdown(f"**{APP_AUTHOR}**")
    st.sidebar.caption(APP_TAGLINE)
    st.sidebar.caption(APP_LOCATION)

    return page