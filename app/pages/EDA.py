import streamlit as st

def main():
    st.title("Statistical Overview of Housing Attributes")

    st.markdown("### **Distribution of Housing Attributes**")
    image_path2 = "app/pages/img2_finalproj.png"
    st.image(image_path2, use_container_width=False, output_format="auto")
    st.write("""
    This visualization shows the distribution of various features such as price, area, bedrooms, bathrooms, stories, and parking.
    The price and area distributions are right-skewed, indicating that most properties fall within lower price and area ranges.
    """)

    st.markdown("### **Price Trends by Furnishing Status and Area Preference**")
    image_path1 = "app/pages/imgt1.png"
    st.image(image_path1, use_container_width=False, output_format="auto")
    st.write("""
    This scatter plot displays how property prices vary based on furnishing status and whether the property is in a preferred area.
    Properties in the preferred area generally have higher prices across all furnishing types.
    """)

    st.markdown("### **Price Trends by Covered Area and Furnishing Status**")
    image_path3 = "app/pages/finaldprojappd_3.png"
    st.image(image_path3, use_container_width=False, output_format="auto")
    st.write("""
    This plot shows the relationship between price and area, with different markers representing the furnishing status.
    A positive correlation exists between price and area, and prices vary significantly based on furnishing status.
    """)

    image_path4 = "app/pages/price_area_apdFP.png"
    st.markdown("### **Trendline Analysis:House Price and Covered Area**")
    st.image(image_path4, use_container_width=False, output_format="auto")
    st.write("""
    This scatter plot illustrates the price distribution against area size.
    Most properties are clustered in the lower area range, but as the area increases, there is a wider spread in prices.
    """)

if __name__ == "__main__":
    main()