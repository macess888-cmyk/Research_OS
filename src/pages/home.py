import streamlit as st

from src.components.dashboard.health_card import render_health_card
from src.components.dashboard.validation_card import render_validation_card
from src.components.dashboard.workspace_card import render_workspace_card


def render_home():

    st.title("Research OS Dashboard")

    render_health_card()

    st.divider()

    render_validation_card()

    st.divider()

    render_workspace_card()