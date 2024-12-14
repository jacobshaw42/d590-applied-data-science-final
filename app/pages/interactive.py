import streamlit as st

def main():
    st.title("House Price Predictorg")
    
    # Input Fields
    st.number_input("Area", placeholder="Enter Area of House")
    st.number_input("Bedrooms",placeholder="Enter no. of bedrooms")
    st.number_input("Bathroom",placeholder="Enter no. of bathrooms")
    st.number_input("Stories",placeholder="Enter no. of stories")
    st.number_input("Parking",placeholder="Enter no.of parking space")
    #st.number_input("Furnishing Status",placeholder="Enter furnishing status, Fully Furnished=2,Semi-Furnished=1,Not Furnished=0")
    #st.number_input("Guestroom",placeholder="Enter 1 if you need guestroom,enter 0 if you dont need guestroom")
    #st.number_input("Hotwater Heating",placeholder="Enter 1 if you want hot water heater,enter 0 if you dont want hot water heater")
    #st.number_input("Preferred Area",placeholder="Enter 1 if you in preferred area, enter 0 if you dont need in pref area")


    #st.checkbox(label="Active")

    Furnishing_Status = ['Furnished','Unfurnished','Semi-Furnished']
    Main_Road = ['Yes', 'No']
    Guestroom = ['Yes', 'No']
    Basement = ['Yes', 'No']
    Hotwater_Heating = ['Yes', 'No']
    Preferred_Area = ['Yes', 'No']

    house_furnishing_status = st.radio(label="House Furnishing Status", options=Furnishing_Status)
    user_main_road = st.radio(label="Select if you need the house near the main road", options=Main_Road)
    user_guestroom = st.radio(label="Do you need a guestroom?", options=Guestroom)
    user_basement = st.radio(label="Do you need a basement?", options=Basement)
    user_hotwater_heating = st.radio(label="Do you want hot water heating?", options=Hotwater_Heating)
    user_preferred_area = st.radio(label="Do you want the house in a preferred area?", options= Preferred_Area)

