import streamlit as st

from src.services.config_service import ConfigService


def render_header():
    config = ConfigService()

    st.title(config.app_name)

    st.caption(
        f"{config.author} • Version {config.version}"
    )

    st.divider()