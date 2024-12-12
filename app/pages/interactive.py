import streamlit as st

def main():
    st.title("This Page should display an interactive ability to input values our of model that returns a predicted value")
    
    # Input Fields
    st.number_input("Area", placeholder="Enter Area of House")
    st.number_input("Bedrooms",placeholder="Enter no. of bedrooms")
    st.number_input("Bathroom",placeholder="Enter no. of bathrooms")
    st.number_input("Stories",placeholder="Enter no. of stories")
    st.number_input("Parking",placeholder="Enter no.of parking space")
    st.number_input("Furnishing Status",placeholder="Enter furnishing status, Fully Furnished=2,Semi-Furnished=1,Not Furnished=0")
    st.number_input("Main Road",placeholder="Enter if you want near main road,YES=1,No=0")
    st.number_input("Guestroom",placeholder="Enter 1 if you need guestroom,enter 0 if you dont need guestroom")
    st.number_input("Basement",placeholder="Enter 1 if you want basement,enter 0 if you dont want basement")
    st.number_input("Hotwater Heating",placeholder="Enter 1 if you want hot water heater,enter 0 if you dont want hot water heater")
    st.number_input("Preferred Area",placeholder="Enter 1 if you in preferred area, enter 0 if you dont need in pref area")