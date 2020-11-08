import streamlit as st 
import app_summarize_intro
import app_summarize_1
import app_summarize_2


PAGES = {
    "Introduction": app_summarize_intro,
    "Summarisation": app_summarize_1,
    "Question Generation": app_summarize_2
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()
