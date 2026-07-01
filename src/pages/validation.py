import streamlit as st

from src.services.validation_engine import ValidationEngine


def render_validation():

    st.header("Research OS Validation")

    st.caption("Inspect the health and integrity of the platform.")

    engine = ValidationEngine()

    report = engine.validate()

    passed = 0
    warnings = 0
    failed = 0

    for status, message in report:

        if status == "PASS":
            st.success(message)
            passed += 1

        elif status == "WARNING":
            st.warning(message)
            warnings += 1

        else:
            st.error(message)
            failed += 1

    st.divider()

    c1, c2, c3 = st.columns(3)

    c1.metric("PASS", passed)
    c2.metric("WARNING", warnings)
    c3.metric("FAIL", failed)

    if failed == 0:
        st.success("Validation completed successfully.")