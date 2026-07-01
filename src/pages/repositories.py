import streamlit as st

from src.services.repository_engine import RepositoryEngine

def render_repositories():

    st.header("Repository Explorer")

    root = st.text_input(
        "Scan Folder",
        value=str(RepositoryEngine().root)
    )

    engine = RepositoryEngine(root)

    repos = engine.repositories()

    st.metric("Repositories Found", len(repos))

    st.divider()

    for repo in repos:

        with st.expander(repo.name):
            st.code(str(repo))