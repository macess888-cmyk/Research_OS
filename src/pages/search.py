import streamlit as st
from src.utils.search import search_content

def render_search():
    st.header("Global Search")
    st.caption("Search all Markdown content in the Research OS content directory.")

    query = st.text_input("Search term")

    if query:
        results = search_content(query)

        st.write(f"Results found: {len(results)}")

        for result in results:
            with st.expander(str(result["path"])):
                for line_no, line in result["matches"]:
                    st.markdown(f"**Line {line_no}:** {line}")