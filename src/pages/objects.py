import streamlit as st
from src.services.object_engine import ObjectEngine


def render_objects():
    engine = ObjectEngine()

    st.header("Research Objects")

    objects = engine.load_all()

    st.metric("Objects", engine.count())

    st.subheader("Object Types")
    for obj_type, count in engine.by_type().items():
        st.write(f"**{obj_type.title()}** — {count}")

    st.divider()

    query = st.text_input("Search Objects")

    if query:
        objects = engine.search(query)

    for obj in objects:
        with st.expander(obj.get("title", obj.get("id", "Untitled"))):
            st.write(f"**ID:** {obj.get('id')}")
            st.write(f"**Type:** {obj.get('type')}")
            st.write(f"**Status:** {obj.get('status', 'UNKNOWN')}")
            st.write(obj.get("summary", ""))

            related = engine.related(obj.get("id"))

            if related:
                st.markdown("### Related")
                for rel in related:
                    st.write(f"• {rel.get('title', rel.get('id'))} ({rel.get('type')})")