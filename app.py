import streamlit as st

# Components
from src.components.header import render_header
from src.components.sidebar import render_sidebar

# Core Pages
from src.pages.home import render_home
from src.pages.biography import render_biography
from src.pages.research import render_research
from src.pages.publications import render_publications
from src.pages.software import render_software
from src.pages.teaching import render_teaching
from src.pages.collaborations import render_collaborations

# Knowledge Pages
from src.pages.atlas import render_atlas
from src.pages.graph import render_graph
from src.pages.registry import render_registry
from src.pages.timeline import render_timeline
from src.pages.search import render_search

# Platform Pages
from src.pages.repositories import render_repositories
from src.pages.workspace import render_workspace
from src.pages.health import render_health

# Administration Pages
from src.pages.admin import render_admin
from src.pages.build_center import render_build_center


ROUTES = {
    "Dashboard": render_home,
    "Biography": render_biography,
    "Research Program": render_research,
    "Publications": render_publications,
    "Software": render_software,
    "Teaching": render_teaching,
    "Collaborations": render_collaborations,
    "Research Atlas": render_atlas,
    "Knowledge Graph": render_graph,
    "Research Registry": render_registry,
    "Timeline": render_timeline,
    "Search": render_search,
    "Repositories": render_repositories,
    "Research Workspace": render_workspace,
    "System Health": render_health,
    "Admin Editor": render_admin,
    "Build Center": render_build_center,
}


def main():
    st.set_page_config(
        page_title="Research OS | Jake Macdonald",
        page_icon="🎓",
        layout="wide"
    )

    page = render_sidebar()
    render_header()

    route = ROUTES.get(page)

    if route:
        route()
    else:
        st.error(f"No route found for page: {page}")


if __name__ == "__main__":
    main()