import streamlit as st

from src.services.navigator_engine import NavigatorEngine


def render_navigator():
    nav = NavigatorEngine()

    st.title("Research Navigator")

    stats = nav.statistics()

    c1, c2 = st.columns(2)

    c1.metric("Objects", stats["objects"])
    c2.metric("Relationships", stats["relationships"])

    st.divider()

    query = st.text_input(
        "Search Research Objects",
        placeholder="Try: observability"
    )

    if not query:
        return

    results = nav.search(query)

    if not results:
        st.warning("No matching research objects found.")
        return

    st.subheader("Results")

    for obj in results:

        with st.expander(obj.get("title", obj["id"])):

            st.write(f"**Type:** {obj.get('type', 'unknown')}")
            st.write(f"**Status:** {obj.get('status', 'UNKNOWN')}")

            if obj.get("summary"):
                st.write(obj["summary"])

            report = nav.explore(obj["id"])

            if report and report["related"]:

                st.markdown("### Related Objects")

                for related in report["related"]:
                    st.write(
                        f"• {related.get('title', related.get('id'))} "
                        f"({related.get('type', 'unknown')})"
                    )

            if report and report["completeness"]:

                comp = report["completeness"]

                st.metric(
                    "Completeness",
                    f"{comp['score']} / {comp['total']}"
                )