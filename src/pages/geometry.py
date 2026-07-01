import streamlit as st

from src.geometry.structural_geometry import StructuralGeometry


def render_geometry():
    inspector = StructuralGeometry()
    report = inspector.inspect()

    st.title("Geometry Framework")
    st.caption("Let geometry have a say.")

    st.subheader(inspector.name)

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Nodes", report["nodes"])
    c2.metric("Edges", report["edges"])
    c3.metric("Density", report["density"])
    c4.metric("Isolated", report["isolated"])

    st.divider()

    st.write(f"**Status:** {report['status']}")
    st.write(f"**Geometry:** {report['geometry']}")

    most = report["most_connected"]

    if most:
        st.success(
            f"Most connected: {most['title']} — {most['degree']} connection(s)"
        )
    else:
        st.info("No central object detected.")