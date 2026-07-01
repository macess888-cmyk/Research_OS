import streamlit as st

from src.services.mission_control import MissionControl


def render_mission_control():

    mc = MissionControl()

    st.title("Mission Control")

    report = mc.platform_report()

    st.caption(f"Generated: {report['time']}")

    st.divider()

    st.subheader("Health")

    for name, value in report["health"].items():
        st.metric(name, value)

    st.divider()

    st.subheader("Validation")

    for status, message in report["validation"]:
        if status == "PASS":
            st.success(message)
        elif status == "WARNING":
            st.warning(message)
        else:
            st.error(message)

    st.divider()

    st.subheader("Research Intelligence")

    for name, value in report["intelligence"].items():
        st.metric(name.replace("_", " ").title(), value)