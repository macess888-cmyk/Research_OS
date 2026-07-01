import streamlit as st

from src.services.graph_engine import GraphEngine


def render_graph():

    graph = GraphEngine()

    st.header("Research Knowledge Graph")

    c1, c2, c3 = st.columns(3)

    c1.metric("Nodes", graph.node_count())
    c2.metric("Relationships", graph.edge_count())
    c3.metric("Types", len(graph.node_types()))

    st.divider()

    st.subheader("Node Types")

    for t, count in graph.node_types().items():
        st.write(f"**{t.title()}** — {count}")

    st.divider()

    st.subheader("Nodes")

    for node in graph.nodes:

        with st.expander(node["label"]):

            st.write(f"Type: **{node['type']}**")

            neighbors = graph.neighbors(node["id"])

            if neighbors:

                st.write("Connected To")

                for n in neighbors:
                    st.write(f"• {n['label']}")