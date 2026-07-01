import streamlit as st

from src.kernel.kernel import ResearchKernel


def render_kernel():
    kernel = ResearchKernel()

    st.title("Research Kernel")

    status = kernel.status()

    c1, c2, c3 = st.columns(3)

    c1.metric("Objects", status["objects"])
    c2.metric("Relationships", status["relationships"])
    c3.metric("Density", status["density"])

    st.divider()

    st.subheader("Kernel Services")

    st.success("✓ Object Engine")
    st.success("✓ Relationship Engine")
    st.success("✓ Navigator Engine")
    st.success("✓ Graph Engine")
    st.success("✓ Analytics Engine")