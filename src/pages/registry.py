import streamlit as st

from src.services.registry_engine import RegistryEngine


def render_registry():

    registry = RegistryEngine()

    st.header("Research Registry")

    st.subheader("Content Summary")

    summary = registry.summary()

    for section, count in summary.items():
        st.write(f"**{section.title()}** — {count} file(s)")

    st.divider()

    st.subheader("Sections")

    for section in registry.all_sections():

        with st.expander(section.title()):

            files = registry.files(section)

            if not files:
                st.write("No content.")

            for file in files:
                st.write(file.relative_to(registry.content))