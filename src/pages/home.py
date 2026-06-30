import streamlit as st
from src.utils.stats import get_dashboard_stats

def render_home():
    st.header("Research Dashboard")
    st.write("Kelowna, British Columbia, Canada")

    st.markdown("""
**Email:** 00jake@orocore.one  
**LinkedIn:** https://linkedin.com/in/jake-macdonald-45394a393  
**ORCID:** https://orcid.org/0009-0000-6513-7049  
**GitHub:** https://github.com/macess888-cmyk/HACR_Hybrid_Observatory
""")

    st.subheader("Live Project Stats")
    stats = get_dashboard_stats()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Markdown Files", stats["Markdown Files"])
    col2.metric("Python Files", stats["Python Files"])
    col3.metric("Images", stats["Images"])
    col4.metric("Git Commits", stats["Git Commits"])

    st.subheader("Research Identity")
    st.write(
        "Independent researcher developing open-source frameworks and software "
        "for AI governance, observability, resilience engineering, and boundary-based "
        "architectures for complex adaptive systems."
    )