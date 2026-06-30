import streamlit as st

def render_home():
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