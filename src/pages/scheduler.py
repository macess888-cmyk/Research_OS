import streamlit as st

from src.services.task_scheduler import TaskScheduler


def render_scheduler():
    scheduler = TaskScheduler()

    st.title("Task Scheduler")
    st.caption("Routine platform maintenance and inspections.")

    summary = scheduler.summary()

    c1, c2, c3 = st.columns(3)

    c1.metric("Registered", summary["registered"])
    c2.metric("Enabled", summary["enabled"])
    c3.metric("Generated", summary["generated"])

    st.divider()

    for task in scheduler.all():
        status = "🟢" if task["enabled"] else "⚪"

        st.write(
            f"{status} **{task['name']}** — {task['frequency']}"
        )