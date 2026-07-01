import streamlit as st

from src.services.platform_registry import PlatformRegistry


def render_platform_registry():
    registry = PlatformRegistry()

    st.title("Platform Registry")
    st.caption("Research OS describing itself.")

    services = registry.services()

    st.metric("Registered Services", len(services))

    st.divider()

    for service in services:

        with st.expander(
            f"{service['name']}  [{service['status']}]",
            expanded=True,
        ):

            details = service.get("details", {})

            if details:
                for key, value in details.items():
                    st.write(f"**{key}:** {value}")
            else:
                st.caption("No additional metadata.")