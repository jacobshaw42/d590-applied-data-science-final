import streamlit as st

selected_page = st.sidebar.selectbox("Go to", ["Home Page", "EDA", "Interactive"])

# Load the selected page
if selected_page == __name__:
    st.title("Home page")
elif selected_page == "EDA":
    from pages import EDA
    EDA.main()
elif selected_page == "Interactive":
    from pages import interactive
    interactive.main()