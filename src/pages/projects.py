import streamlit as st
from src.services.project_engine import ProjectEngine


def render_projects():
    engine = ProjectEngine()

    st.header("Project Hub")
    st.metric("Projects", engine.count())

    st.divider()

    for project in engine.projects():
        with st.expander(project["name"]):
            st.write(f"**Status:** {project['status']}")
            st.write(f"**Category:** {project['category']}")
            st.write(project["description"])

            if project["github"]:
                st.write(f"**GitHub:** {project['github']}")