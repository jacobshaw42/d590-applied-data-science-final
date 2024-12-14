import streamlit as st

def main():
    st.title("House Price Predictor")
    
    # Input Fields
    area = st.number_input("Area", placeholder="Enter Area of House")
    beds = st.number_input("Bedrooms",placeholder="Enter no. of bedrooms")
    baths = st.number_input("Bathroom",placeholder="Enter no. of bathrooms")
    stories = st.number_input("Stories",placeholder="Enter no. of stories")
    parking = st.number_input("Parking",placeholder="Enter no.of parking space")
    furnish = st.number_input("Furnishing Status",placeholder="Enter furnishing status, Fully Furnished=2,Semi-Furnished=1,Not Furnished=0")
    air = st.number_input("Air Conditioning",placeholder="Enter 1 if you have air conditioning, enter 0 if you dont need air conditioning")
    
    Furnishing_Status = ['Yes', 'No']
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
    
    if  st.button("Submit"):
        import os
        from .utils import main as create_model
        import joblib
        import numpy as np
        
        ml_path = "LinearModel.joblib"
        if not os.path.exists(ml_path):
            model = create_model()
        else:
            model = joblib.load(ml_path)
        
        if user_basement == "Yes":
            basement_no, basement_yes = 0,1
        else:
            basement_no, basement_yes = 1,0
        if user_main_road == "Yes":
            road_no, road_yes = 0,1 
        else:
            road_no , road_yes = 1,0
        if user_guestroom == "Yes":
            guestroom_no, guestroom_yes = 0,1
        else:
            guestroom_no, guestroom_yes = 1,0 
        if user_hotwater_heating == "Yes":
            hot_water_no, hot_water_yes = 0,1
        else:
            hot_water_no, hot_water_yes = 1,0
        if air == 1:
            air_no, air_yes = 0,1
        else:
            air_no, air_yes = 1,0
        if user_preferred_area == "Yes":
            pre_area_no, pre_area_yes = 0,1
        else:
            pre_area_no, pre_area_yes = 1,0
        
        x = np.array([[
            area,beds,baths,stories,parking,furnish,
            road_no, road_yes,
            guestroom_no, guestroom_yes,
            basement_no,basement_yes,
            hot_water_no, hot_water_yes,
            air_no, air_yes,
            pre_area_no, pre_area_yes
        ]])
        pred = model.predict(x)[0]
        st.write(f"The predicted cost of this home should be ${pred:,.2f}")
