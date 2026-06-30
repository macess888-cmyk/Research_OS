import streamlit as st

from src.utils.registry import list_projects

def render_software():

    st.header("Software Gallery")

    for project in list_projects():

        with st.expander(project.stem.replace("_", " ").title()):

            st.markdown(project.read_text(encoding="utf-8"))