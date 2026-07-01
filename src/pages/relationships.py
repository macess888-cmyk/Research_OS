import streamlit as st

from src.services.relationship_engine import RelationshipEngine
from src.services.object_engine import ObjectEngine


def render_relationships():

    objects = ObjectEngine()
    engine = RelationshipEngine()

    st.title("Relationship Explorer")

    st.metric(
        "Relationships",
        engine.relationship_count()
    )

    st.divider()

    names = {
        obj["title"]: obj["id"]
        for obj in objects.load_all()
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
            st.write(f"• {item}")
    else:
        st.info("No relationships.")

    st.divider()

    st.subheader("Completeness")

    report = engine.completeness(object_id)

    st.metric(
        "Score",
        f"{report['score']} / {report['total']}"
    )

    for key, value in report["checks"].items():

        if value:
            st.success(key)

        else:
            st.warning(key)

    st.divider()

    st.subheader("Orphan Objects")

    orphans = engine.orphan_objects()

    if not orphans:
        st.success("No orphan objects detected.")
    else:
        for obj in orphans:
            st.warning(obj["title"])