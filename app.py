import streamlit as st
from pathlib import Path

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="Jake Macdonald Academic Portfolio",
    page_icon="🎓",
    layout="wide"
)

def load_md(path):
    file_path = ROOT / path
    if file_path.exists():
        return file_path.read_text(encoding="utf-8")
    return f"Missing file: {path}"

st.title("Jake Macdonald")
st.subheader("Academic Portfolio & Research Dossier")

st.write("Hybrid Systems Architect • Founder, HACR Hybrid Observatory")
st.write("Kelowna, British Columbia, Canada")

st.markdown("""
**LinkedIn:** https://linkedin.com/in/jake-macdonald-45394a393  
**ORCID:** https://orcid.org/0009-0000-6513-7049  
**GitHub:** https://github.com/macess888-cmyk/HACR_Hybrid_Observatory
""")

tab1, tab2, tab3, tab4 = st.tabs([
    "Biography",
    "Publications",
    "Software",
    "Teaching"
])

with tab1:
    st.markdown(load_md("biography/faculty_bio.md"))

with tab2:
    st.markdown(load_md("publications/orcid.md"))

with tab3:
    st.markdown(load_md("software/hacr.md"))

with tab4:
    st.markdown(load_md("teaching/teaching_statement.md"))