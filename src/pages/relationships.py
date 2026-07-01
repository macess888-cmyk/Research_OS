import streamlit as st

from src.services.relationship_engine import RelationshipEngine
from src.services.object_engine import ObjectEngine


def render_relationships():
    objects = ObjectEngine()
    engine = RelationshipEngine()

    st.title("Relationship Explorer")

    st.metric("Relationships", engine.relationship_count())

    st.divider()

    loaded_objects = objects.load_all()

    names = {
        obj.get("title", obj.get("id")): obj.get("id")
        for obj in loaded_objects
        if obj.get("id")
    }

    selected = st.selectbox(
        "Select Object",
        sorted(names.keys())
    )

    object_id = names[selected]

    st.subheader("Connected Objects")

    related = engine.related(object_id)

    if related:
        for item in related:
            st.markdown(
                f"**{item.get('title', item.get('id'))}** "
                f"({item.get('type', 'unknown')})"
            )
    else:
        st.info("No relationships.")

    st.divider()

    st.subheader("Completeness")

    report = engine.completeness(object_id)

    if report:
        st.metric(
            "Score",
            f"{report['score']} / {report['total']}"
        )

        for key, value in report["checks"].items():
            if value:
                st.success(key)
            else:
                st.warning(key)
    else:
        st.error("No completeness report available.")

    st.divider()

    st.subheader("Orphan Objects")

    orphans = engine.orphan_objects()

    if not orphans:
        st.success("No orphan objects detected.")
    else:
        for obj in orphans:
            st.warning(obj.get("title", obj.get("id")))