import streamlit as st

from src.config import APP_NAME, APP_VERSION, APP_AUTHOR, APP_TAGLINE, APP_LOCATION

PAGES = [
    "Dashboard",
    "Mission Control",

    # Platform
    "System Health",
    "Validation",
    "Research Intelligence",
    "Platform Analytics",
    "Research Kernel",

    # Research
    "Biography",
    "Research Program",
    "Publications",
    "Teaching",
    "Collaborations",

    # Projects
    "Project Hub",
    "Software",
    "Repositories",
    "Research Workspace",

    # Knowledge
    "Research Atlas",
    "Knowledge Graph",
    "Graph Metrics",
    "Research Registry",
    "Research Objects",
    "Object Registry",
    "Relationship Explorer",
    "Research Navigator",
    "Timeline",
    "Search",

    # Administration
    "About",
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