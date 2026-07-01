import streamlit as st

from src.graph.graph_engine import GraphEngineV2


def render_graph_metrics():
    graph = GraphEngineV2()

    st.title("Graph Metrics")

    c1, c2, c3 = st.columns(3)

    c1.metric("Nodes", graph.node_count())
    c2.metric("Edges", graph.edge_count())
    c3.metric("Density", graph.density())

    st.divider()

    st.subheader("Most Connected Object")

    most = graph.most_connected()

    if most:
        st.success(
            f"{most['title']} — {most['degree']} connection(s)"
        )
    else:
        st.info("No connected objects found.")

    st.divider()

    st.subheader("Isolated Nodes")

    isolated = graph.isolated_nodes()

    if not isolated:
        st.success("No isolated nodes detected.")
    else:
        for node in isolated:
            st.warning(node.get("title", node.get("id")))