import streamlit as st

from src.services.platform_registry import PlatformRegistry


def render_platform_registry():
    registry = PlatformRegistry()

    st.title("Platform Registry")
    st.caption("Research OS describing itself through inspectable services.")

    services = registry.services()

    st.metric("Registered Services", registry.count())

    st.divider()

    for service in services:
        name = service.get("service", "Unnamed Service")
        status = service.get("status", "UNKNOWN")
        healthy = service.get("healthy", False)

        label = f"{name} [{status}]"

        with st.expander(label, expanded=True):
            if healthy:
                st.success("Healthy")
            else:
                st.warning("Needs inspection")

            for key, value in service.items():
                if key in ["service", "status", "healthy"]:
                    continue

                st.write(f"**{key.replace('_', ' ').title()}:** {value}")