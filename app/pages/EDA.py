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

    image_paths = "app/pages/imgt1.png"
    st.image(image_paths, caption="EDA1", use_column_width=False, output_format="auto")