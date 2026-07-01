import streamlit as st

from src.services.object_engine import ObjectEngine


def render_object_registry():
    engine = ObjectEngine()

    st.title("Research Object Registry")

    objects = engine.load_all()

    st.metric("Registered Objects", len(objects))

    st.divider()

    for obj in sorted(objects, key=lambda x: x.get("title", "")):

        with st.expander(obj.get("title", obj.get("id"))):

            col1, col2 = st.columns(2)

            col1.write(f"**ID**: {obj.get('id')}")
            col1.write(f"**Type**: {obj.get('type')}")

            col2.write(f"**Status**: {obj.get('status','UNKNOWN')}")
            col2.write(f"**Source**: {obj.get('_file')}")

            if obj.get("summary"):
                st.write(obj["summary"])

            related = engine.related(obj["id"])

            if related:
                st.markdown("### Related Objects")

                for r in related:
                    st.write(f"• {r.get('title', r.get('id'))}")