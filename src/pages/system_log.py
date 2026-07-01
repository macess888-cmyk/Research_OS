import streamlit as st

from src.services.logging_service import LoggingService


def render_system_log():
    logger = LoggingService()

    st.title("System Log")

    if st.button("Write Test Log"):
        logger.info(
            "System Log",
            "Test log entry created."
        )
        st.success("Log written.")

    st.divider()

    for line in reversed(logger.read()):
        st.code(line.strip())