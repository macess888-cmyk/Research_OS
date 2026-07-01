import streamlit as st

from src.services.topology_engine import TopologyEngine


def render_topology():
    topology = TopologyEngine()

    st.title("Topology Inspector")
    st.caption("Let geometry have a say.")

    summary = topology.summary()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Nodes", summary["nodes"])
    c2.metric("Edges", summary["edges"])
    c3.metric("Density", summary["density"])
    c4.metric("Avg Degree", summary["average_degree"])

    st.divider()

    st.subheader("Central Object")

    central = summary["most_connected"]

    if central:
        st.success(f"{central['title']} — {central['degree']} connection(s)")
    else:
        st.info("No central object detected.")

    st.divider()

    st.subheader("Boundary / Isolation Check")

    report = topology.boundary_report()

    if report["isolated"]:
        for node in report["isolated"]:
            st.warning(node.get("title", node.get("id")))
    else:
        st.success("No isolated nodes detected.")