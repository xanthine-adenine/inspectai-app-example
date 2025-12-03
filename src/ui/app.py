import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Inspect AI App Example",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Title
st.title("🔍 Inspect AI App Example")

# Sidebar
with st.sidebar:
    st.header("Navigation")
    st.write("Welcome to the Inspect AI App Example")

# Main content
st.write("## Welcome")
st.write("This is a simple example of building an app that uses the Inspect framework.")

# Add some example sections
col1, col2 = st.columns(2)

with col1:
    st.subheader("Getting Started")
    st.write("Use the sidebar to navigate through the app.")

with col2:
    st.subheader("Status")
    st.success("Application is running successfully")

# Footer
st.divider()
st.caption("Powered by Streamlit and Inspect AI")
