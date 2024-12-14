import streamlit as st

def main():
    st.title("This page displays our EDA!")

    st.image("app/pages/relplot.png", caption="EDA1", use_container_width=False, output_format="auto")

    image_paths = "app/pages/imgt1.png"
    st.image(image_paths, caption="EDA2", use_container_width=False, output_format="auto")
