import streamlit as st
from pathlib import Path

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="Jake Macdonald Research Portfolio",
    page_icon="🎓",
    layout="wide"
)

def load_md(path):
    file_path = ROOT / path
    if file_path.exists():
        return file_path.read_text(encoding="utf-8")
    return f"Missing file: {path}"

st.sidebar.title("Research Portfolio")

page = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Biography",
        "Research Program",
        "Publications",
        "Software",
        "Teaching",
        "Collaborations",
        "Timeline",
    ]
)

st.title("Jake Macdonald")
st.caption("Hybrid Systems Architect • Founder, HACR Hybrid Observatory")

if page == "Home":
    st.header("Academic Portfolio & Research Dossier")
    st.write("Kelowna, British Columbia, Canada")
    st.markdown("""
    **Email:** 00jake@orocore.one  
    **LinkedIn:** https://linkedin.com/in/jake-macdonald-45394a393  
    **ORCID:** https://orcid.org/0009-0000-6513-7049  
    **GitHub:** https://github.com/macess888-cmyk/HACR_Hybrid_Observatory
    """)

    col1, col2, col3 = st.columns(3)
    col1.metric("Research Program", "Active")
    col2.metric("Publications", "2 DOI Works")
    col3.metric("Software", "Active")

    st.subheader("Research Identity")
    st.write(
        "Independent researcher developing open-source frameworks and software "
        "for AI governance, observability, resilience engineering, and boundary-based "
        "architectures for complex adaptive systems."
    )

elif page == "Biography":
    st.markdown(load_md("biography/faculty_bio.md"))
    st.markdown(load_md("biography/executive_summary.md"))

elif page == "Research Program":
    st.header("Observability and Governability of Complex Systems")
    st.write(
        "This research program investigates how complex technical systems remain "
        "observable, governable, recoverable, and resilient under uncertainty."
    )

elif page == "Publications":
    st.markdown(load_md("publications/orcid.md"))

elif page == "Software":
    st.markdown(load_md("software/hacr.md"))

elif page == "Teaching":
    st.markdown(load_md("teaching/teaching_statement.md"))

elif page == "Collaborations":
    st.header("Collaborations")
    st.write(
        "Collaborative work is presented with clear attribution, distinguishing "
        "individual research, shared research, and external project ownership."
    )

elif page == "Timeline":
    st.header("Research Timeline")
    st.markdown("""
    Invariant Corridors  
    ↓  
    Governance Architectures  
    ↓  
    HACR Hybrid Observatory  
    ↓  
    Universal Bridge  
    ↓  
    Signal Enhancer  
    ↓  
    Governability Break Surface Analysis  
    ↓  
    Recovery Navigation
    """)