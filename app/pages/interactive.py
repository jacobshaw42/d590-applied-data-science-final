import streamlit as st

def main():
    st.title("This Page should display an interactive ability to input values our of model that returns a predicted value")
    
    # Input Fields
    st.number_input("Area", placeholder="Enter Area of House",max_chars=5)
    st.number_input("Bedrooms",placceholder="Enter no. of bedrooms",max_chars=2)
    st.number_input("Bathroom",placeholder="Enter no. of bathrooms",max_chars=2)
    st.number_input("Stories",placeholder="Enter no. of stories",max_chars=1)
    st.number_input("Parking",placeholder="Enter no.of parking space",max_chars=1)
    st.number_input("Furnishing Status",placeholder="Enter furnishing status, Fully Furnished=2,Semi-Furnished=1,Not Furnished=0",max_chars=1)
    st.number_input("Main Road",placeholder="Enter if you want near main road,YES=1,No=0",max_chars=1)
    st.nnumber_input("Guestroom,placeholder="Enter 1 if you need guestroom,enter 0 if you dont need guestroom",max_chars=1)
    st.number_input("Basement,placeholder="Enter 1 if you want basement,enter 0 if you dont want basement",max_chars=1)
    st.number_input("Hotwater Heating,placeholder=Enter 1 if you want hot water heater,enter 0 if you dont want hot water heater,max_chars=1)
    st.number_input("Preferred Area,placeholder= Enter 1 if you in preferred area, enter 0 if you dont need in pref area",max_chars=1)