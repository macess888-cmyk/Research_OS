import streamlit as st

from src.services.intelligence_engine import IntelligenceEngine


def render_intelligence():

    engine = IntelligenceEngine()

    st.header("Research Intelligence")

    summary = engine.summary()

    c1, c2, c3 = st.columns(3)

    c1.metric("Content Files", summary["files"])
    c2.metric("Knowledge Nodes", summary["graph_nodes"])
    c3.metric("Relationships", summary["graph_edges"])

    st.divider()

    st.subheader("Knowledge Graph")

    st.metric("Density", engine.graph_density())

    st.divider()

    st.subheader("Orphan Nodes")

    orphaned = engine.orphan_nodes()

    if orphaned:

        for node in orphaned:
            st.warning(node["label"])

    else:
        st.success("No orphan nodes detected.")