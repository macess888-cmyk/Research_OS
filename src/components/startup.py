import streamlit as st

from src.context import context


def render_startup():

    st.caption(
        f"{context.app_name} {context.version}"
    )