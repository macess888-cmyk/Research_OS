import streamlit as st

from src.components.header import render_header
from src.components.sidebar import render_sidebar

from src.pages.build_center import render_build_center
from src.pages.atlas import render_atlas
from src.pages.admin import render_admin
from src.pages.home import render_home
from src.pages.biography import render_biography
from src.pages.research import render_research
from src.pages.publications import render_publications
from src.pages.software import render_software
from src.pages.teaching import render_teaching
from src.pages.collaborations import render_collaborations
from src.pages.timeline import render_timeline

st.set_page_config(
    page_title="Jake Macdonald Research Portfolio",
    page_icon="🎓",
    layout="wide"
)

page = render_sidebar()
render_header()

if page == "Dashboard":
    render_home()
elif page == "Biography":
    render_biography()
elif page == "Research Program":
    render_research()
elif page == "Publications":
    render_publications()
elif page == "Software":
    render_software()
elif page == "Teaching":
    render_teaching()
elif page == "Collaborations":
    render_collaborations()
elif page == "Research Atlas":
    render_atlas()
elif page == "Timeline":
    render_timeline()
elif page == "Admin Editor":
    render_admin()
elif page == "Build Center":
    render_build_center()