import streamlit as st

from src.services.graph_service import load_graph

def render_graph():
    st.header("Knowledge Graph")

    graph = load_graph()

    st.subheader("Nodes")

    for node in graph["nodes"]:
        st.write(
            f"• {node['label']} "
            f"({node['type']})"
        )

    st.subheader("Relationships")

    for edge in graph["edges"]:
        st.write(
            f"{edge['from']} "
            f"— {edge['relation']} → "
            f"{edge['to']}"
        )