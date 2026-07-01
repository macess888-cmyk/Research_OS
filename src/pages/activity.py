import streamlit as st

from src.services.event_engine import EventEngine


def render_activity():
    events = EventEngine()

    st.title("Activity Log")

    st.metric("Events", events.count())

    st.divider()

    if st.button("Record Test Event"):
        events.publish(
            category="System",
            action="Test event recorded",
            status="INFO",
        )
        st.success("Test event recorded.")

    st.divider()

    for event in events.recent(25):
        status = event.get("status", "INFO")
        line = (
            f"**{event.get('timestamp')}** — "
            f"{event.get('category')} — "
            f"{event.get('action')}"
        )

        if status == "PASS" or status == "SUCCESS":
            st.success(line)
        elif status == "WARNING":
            st.warning(line)
        elif status == "FAIL" or status == "ERROR":
            st.error(line)
        else:
            st.info(line)