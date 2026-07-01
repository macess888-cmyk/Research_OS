import streamlit as st

from src.config import APP_NAME, APP_VERSION
from src.profile import (
    NAME,
    TITLE,
    ORGANIZATION,
    LOCATION,
    EMAIL,
    LINKEDIN,
    ORCID,
    GITHUB,
    RESEARCH_OS,
    HACR,
)


def render_about():

    st.header("About Research OS")

    st.markdown(
        """
Research OS is a modular research management platform designed to support
academic portfolios, publications, software projects, knowledge graphs,
collaborations, teaching material, and automated dossier generation.
"""
    )

    st.divider()

    st.subheader("Research Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.write(f"**Name:** {NAME}")
        st.write(f"**Title:** {TITLE}")
        st.write(f"**Organization:** {ORGANIZATION}")
        st.write(f"**Location:** {LOCATION}")

    with col2:
        st.write(f"**Email:** {EMAIL}")
        st.write(f"**LinkedIn:** {LINKEDIN}")
        st.write(f"**ORCID:** {ORCID}")
        st.write(f"**GitHub:** {GITHUB}")

    st.divider()

    st.subheader("Projects")

    st.markdown(f"**Research OS**  \n{RESEARCH_OS}")

    st.markdown(f"**HACR Hybrid Observatory**  \n{HACR}")

    st.divider()

    st.subheader("Platform")

    st.write(f"**Application:** {APP_NAME}")
    st.write(f"**Version:** {APP_VERSION}")

    st.success("Research OS is under active development.")

    st.divider()

    st.subheader("Mission")

    st.markdown(
        """
Research OS brings together research, software, publications,
knowledge management, and reproducible academic outputs into a
single open-source platform.

The long-term goal is to provide reusable infrastructure for
independent researchers, academic groups, and collaborative
engineering projects.
"""
    )