import streamlit as st

from src.services.health_engine import HealthEngine


def render_health_card():

    engine = HealthEngine()

    report = engine.report()

    st.subheader("Research Health")

    cols = st.columns(len(report))

    for col, (name, value) in zip(cols, report.items()):
        col.metric(name, value)