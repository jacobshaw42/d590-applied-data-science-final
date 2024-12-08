import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import kagglehub

def main():
    st.title("Factors Affecting House Prices")

    path = os.path.expanduser("~/.cache/kagglehub/datasets/yasserh/housing-prices-dataset/versions/1/Housing.csv")
    if not os.path.exists(path):
        kagglehub.dataset_download("yasserh/housing-prices-dataset", force_download=True)

    df = pd.read_csv(path)

    fig = plt.figure(figsize=(20, 10))
    df.hist(figsize=(20, 10))
    st.pyplot(fig)

if __name__ == "__main__":
    main()



