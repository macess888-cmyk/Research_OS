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
from src.pages.mission_control import render_mission_control

# Project Pages
from src.pages.projects import render_projects
from src.pages.repositories import render_repositories
from src.pages.workspace import render_workspace

# Knowledge Pages
from src.pages.atlas import render_atlas
from src.pages.graph import render_graph
from src.pages.graph_metrics import render_graph_metrics
from src.pages.topology import render_topology
from src.pages.registry import render_registry
from src.pages.timeline import render_timeline
from src.pages.search import render_search
from src.pages.objects import render_objects
from src.pages.object_registry import render_object_registry
from src.pages.relationships import render_relationships
from src.pages.navigator import render_navigator

# Platform Pages
from src.pages.health import render_health
from src.pages.validation import render_validation
from src.pages.intelligence import render_intelligence
from src.pages.analytics import render_analytics
from src.pages.kernel import render_kernel
from src.pages.activity import render_activity
from src.pages.system_log import render_system_log
from src.pages.platform_registry import render_platform_registry
from src.pages.doctrine import render_doctrine

# Administration Pages
from src.pages.about import render_about
from src.pages.admin import render_admin
from src.pages.build_center import render_build_center


ROUTES = {
    # Dashboard
    "Dashboard": render_home,
    "Mission Control": render_mission_control,
    "Activity Log": render_activity,

    # Platform
    "System Health": render_health,
    "Validation": render_validation,
    "Research Intelligence": render_intelligence,
    "Platform Analytics": render_analytics,
    "Research Kernel": render_kernel,
    "Platform Registry": render_platform_registry,
    "System Log": render_system_log,
    "Design Doctrine": render_doctrine,

    # Research
    "Biography": render_biography,
    "Research Program": render_research,
    "Publications": render_publications,
    "Teaching": render_teaching,
    "Collaborations": render_collaborations,

    # Projects
    "Project Hub": render_projects,
    "Software": render_software,
    "Repositories": render_repositories,
    "Research Workspace": render_workspace,

    # Knowledge
    "Research Atlas": render_atlas,
    "Knowledge Graph": render_graph,
    "Graph Metrics": render_graph_metrics,
    "Topology Inspector": render_topology,
    "Research Registry": render_registry,
    "Research Objects": render_objects,
    "Object Registry": render_object_registry,
    "Relationship Explorer": render_relationships,
    "Research Navigator": render_navigator,
    "Timeline": render_timeline,
    "Search": render_search,

    # Administration
    "About": render_about,
    "Admin Editor": render_admin,
    "Build Center": render_build_center,
}


def main():
    st.set_page_config(
        page_title="Research OS | Jake Macdonald",
        page_icon="🎓",
        layout="wide",
    )

    page = render_sidebar()
    render_header()

    route = ROUTES.get(page)

    if route is None:
        st.error(f"Unknown page: {page}")
        st.stop()

    route()


if __name__ == "__main__":
    main()