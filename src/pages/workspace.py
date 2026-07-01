import streamlit as st
from src.services.workspace_engine import WorkspaceEngine


def render_workspace():
    ws = WorkspaceEngine()

    st.header("Research Workspace")
    st.metric("Repositories", ws.count())

    st.subheader("Categories")
    for category, count in ws.categories().items():
        st.write(f"**{category}** — {count}")

    st.divider()

    st.subheader("Registered Repositories")
    for repo in ws.repositories():
        with st.expander(repo["name"]):
            st.write(f"**Status:** {repo['status']}")
            st.write(f"**Category:** {repo['category']}")
            st.write(f"**Path:** `{repo['path']}`")

            if repo["github"]:
                st.write(f"**GitHub:** {repo['github']}")