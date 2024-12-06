import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.write("Hello ,let's learn how to build a streamlit app together")

fig, ax = plt.subplots()
df = pd.read_csv("housing-prices-dataset.zip")
df.hist(figsize=(20,10), ax=ax)
st.pyplot(fig)