import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    import os
    import kagglehub
    st.title("Factors Effecting House Prices")

    path="~/.cache/kagglehub/datasets/yasserh/housing-prices-dataset/versions/1/Housing.csv"
    if not os.path.exists(path):
        path1 = kagglehub.dataset_download("yasserh/housing-prices-dataset", force_download=True)

    fig, ax = plt.subplots()
    df = pd.read_csv(path)
    df.hist(figsize=(20,10), ax=ax)
    st.pyplot(fig)

    fig, ax = plt.subplots()
    df = pd.read_csv(path)
    df.hist(figsize=(20,10), ax=ax)
    st.pyplot(fig)
