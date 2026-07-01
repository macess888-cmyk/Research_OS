import streamlit as st

from src.services.workspace_engine import WorkspaceEngine


def render_workspace_card():

    ws = WorkspaceEngine()

    st.subheader("Workspace")

    st.metric("Repositories", ws.count())