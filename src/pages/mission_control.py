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

    st.divider()

    st.subheader("Graph Intelligence")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Nodes", report["graph"]["nodes"])
    c2.metric("Edges", report["graph"]["edges"])
    c3.metric("Density", report["graph"]["density"])
    c4.metric("Isolated", report["graph"]["isolated"])

    st.write(f"**Most Connected:** {report['graph']['most_connected']}")