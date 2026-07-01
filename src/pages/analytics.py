import streamlit as st

from src.services.analytics_engine import AnalyticsEngine


def render_analytics():
    engine = AnalyticsEngine()

    st.title("Platform Analytics")

    summary = engine.summary()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Objects", summary["objects"])
    c2.metric("Relationships", summary["relationships"])
    c3.metric("Density", summary["graph_density"])
    c4.metric("Issues", engine.issue_count())

    st.divider()

    st.subheader("Object Types")

    for obj_type, count in summary["object_types"].items():
        st.write(f"**{obj_type.title()}** — {count}")

    st.divider()

    st.subheader("Quality Report")

    report = engine.quality_report()

    for item in report:
        with st.expander(item["title"]):
            st.write(f"**Type:** {item['type']}")

            completeness = item.get("completeness")

            if completeness:
                st.metric(
                    "Completeness",
                    f"{completeness['score']} / {completeness['total']}"
                )

            if item["issues"]:
                for issue in item["issues"]:
                    st.warning(issue)
            else:
                st.success("No issues detected.")