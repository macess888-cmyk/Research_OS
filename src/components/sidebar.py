import streamlit as st

PAGES = [
    "Dashboard",
    "System Health",

    "Biography",
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

    "Admin Editor",
    "Build Center",
]

def render_sidebar():
    st.sidebar.title("Research OS")
    st.sidebar.caption("Research OS v1.7.0")

    st.sidebar.markdown("---")
    page = st.sidebar.radio("Navigate", PAGES)

    st.sidebar.markdown("---")
    st.sidebar.markdown("**Jake Macdonald**")
    st.sidebar.caption("Hybrid Systems Architect")
    st.sidebar.caption("Kelowna, BC, Canada")

    return page