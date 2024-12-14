import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    import os
    import kagglehub

    st.title("This page displays our EDA!")

    path="~/.cache/kagglehub/datasets/yasserh/housing-prices-dataset/versions/1/Housing.csv"
    if not os.path.exists(path):
        path1 = kagglehub.dataset_download("yasserh/housing-prices-dataset", force_download=True)

    fig, ax = plt.subplots()
    df = pd.read_csv(path)
    df.hist(figsize=(20,10), ax=ax)
    st.pyplot(fig)

    image_path1 = "app/pages/imgt1.png"
    st.image(image_path1, caption="EDA1", use_container_width=False, output_format="auto")

    image_path1 = "app/pages/img2_finalproj.png"
    st.image(image_path1, caption="EDA2", use_container_width=False, output_format="auto")