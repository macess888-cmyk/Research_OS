import streamlit as st

from src.services.config_service import ConfigService


PAGES = [
    "Dashboard",
    "Mission Control",
    "Activity Log",

    # Platform
    "System Health",
    "Validation",
    "Research Intelligence",
    "Platform Analytics",
    "Research Kernel",
    "Platform Registry",
    "Design Doctrine",
    "System Log",

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
    "Topology Inspector",
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
    config = ConfigService()

    st.sidebar.title(config.app_name)
    st.sidebar.caption(f"v{config.version}")

    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "Navigate",
        PAGES,
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown(f"**{config.author}**")
    st.sidebar.caption(config.get("application", "organization"))

    return page