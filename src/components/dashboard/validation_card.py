import streamlit as st

from src.services.validation_engine import ValidationEngine


def render_validation_card():

    engine = ValidationEngine()

    report = engine.validate()

    passed = len([r for r in report if r[0] == "PASS"])
    warnings = len([r for r in report if r[0] == "WARNING"])
    failed = len([r for r in report if r[0] == "FAIL"])

    st.subheader("Validation")

    c1, c2, c3 = st.columns(3)

    c1.metric("PASS", passed)
    c2.metric("Warnings", warnings)
    c3.metric("Failures", failed)