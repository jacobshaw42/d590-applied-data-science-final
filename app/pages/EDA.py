import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def main():
    import os
    import kagglehub

    st.title("EDA Page")

    # path="~/.cache/kagglehub/datasets/yasserh/housing-prices-dataset/versions/1/Housing.csv"
    # if not os.path.exists(path):
    #     path1 = kagglehub.dataset_download("yasserh/housing-prices-dataset", force_download=True)

    # fig, ax = plt.subplots()
    # df = pd.read_csv(path)
    # df.hist(figsize=(20,10), ax=ax)
    # st.pyplot(fig)

    st.markdown("### **Single Variable Visualizations**")
    image_path2 = "app/pages/img2_finalproj.png"
    st.image(image_path2, use_container_width=False, output_format="auto")
    st.write("""
    This visualization shows the distribution of various features such as price, area, bedrooms, bathrooms, stories, and parking.
    The price and area distributions are right-skewed, indicating that most properties fall within lower price and area ranges.
    """)

    st.markdown("### **Price By Furnishing Status**")
    image_path1 = "app/pages/imgt1.png"
    st.image(image_path1, use_container_width=False, output_format="auto")
    st.write("""
    This scatter plot displays how property prices vary based on furnishing status and whether the property is in a preferred area.
    Properties in the preferred area generally have higher prices across all furnishing types.
    """)

    st.markdown("### **Price & Area with Furnishing Status**")
    image_path3 = "app/pages/finaldprojappd_3.png"
    st.image(image_path3, use_container_width=False, output_format="auto")
    st.write("""
    This plot shows the relationship between price and area, with different markers representing the furnishing status.
    A positive correlation exists between price and area, and prices vary significantly based on furnishing status.
    """)

    image_path4 = "app/pages/price_area_apdFP.png"
    st.markdown("### **Price by Area**")
    st.image(image_path4, use_container_width=False, output_format="auto")
    st.write("""
    This scatter plot illustrates the price distribution against area size.
    Most properties are clustered in the lower area range, but as the area increases, there is a wider spread in prices.
    """)