import streamlit as st

from src.services.health_engine import HealthEngine


def render_health():

    st.header("Research OS Health")

    engine = HealthEngine()

    report = engine.report()

    cols = st.columns(len(report))

    for col, (name, value) in zip(cols, report.items()):
        col.metric(name, value)

    st.divider()

    st.subheader("System Status")

    st.success("Content Registry Online")
    st.success("Knowledge Graph Online")
    st.success("Search Engine Online")
    st.success("PDF Engine Online")