import streamlit as st


# --- PAGE SETUP ---

project_1_page = st.Page(
    page='app.py',
    title=" Dashboard",
    icon=":material/youtube_activity:",
)
project_2_page = st.Page(
    page='assistant.py',
    title="Chat Bot",
    icon=":material/smart_toy:",
)
# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Main": [project_1_page, project_2_page],
    }
)


st.sidebar.markdown("Made with ❤️ by students of rlsibca & Powered by Streamlit😎,GiminiPro🤖&Python👨‍💻")


# --- RUN NAVIGATION ---
pg.run()

