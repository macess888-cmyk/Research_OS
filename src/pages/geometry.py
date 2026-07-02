import streamlit as st

from src.geometry.structural_geometry import StructuralGeometry


def render_geometry():
    inspector = StructuralGeometry()
    report = inspector.inspect()

    st.title("Geometry Framework")
    st.caption("Let geometry have a say.")

    st.subheader(report.get("service", inspector.name))

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Nodes", report.get("nodes", 0))
    c2.metric("Edges", report.get("edges", 0))
    c3.metric("Density", report.get("density", 0))
    c4.metric("Isolated", report.get("isolated", 0))

    st.divider()

    st.write(f"**Status:** {report.get('status', 'UNKNOWN')}")

    if report.get("healthy", False):
        st.success("Geometry inspection completed successfully.")
    else:
        st.warning("Geometry inspection requires attention.")

    st.write(f"**Geometry:** {report.get('geometry', 'UNKNOWN → HOLD')}")

    st.divider()

    st.subheader("Network Centre")

    most = report.get("most_connected")

    if most and most != "None":
        st.success(f"Most connected object: {most}")
    else:
        st.info("No central object detected.")

    st.divider()

    st.subheader("Inspection Report")

    for key, value in report.items():
        if key in {
            "service",
            "status",
            "healthy",
            "nodes",
            "edges",
            "density",
            "isolated",
            "most_connected",
            "geometry",
        }:
            continue

        st.write(f"**{key.replace('_', ' ').title()}:** {value}")