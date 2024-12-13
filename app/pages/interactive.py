import streamlit as st

def main():
    st.title("This Page should display an interactive ability to input values our of model that returns a predicted value")
    
    # Input Fields
    area = st.number_input("Area", placeholder="Enter Area of House")
    beds = st.number_input("Bedrooms",placeholder="Enter no. of bedrooms")
    baths = st.number_input("Bathroom",placeholder="Enter no. of bathrooms")
    stories = st.number_input("Stories",placeholder="Enter no. of stories")
    parking = st.number_input("Parking",placeholder="Enter no.of parking space")
    furnish = st.number_input("Furnishing Status",placeholder="Enter furnishing status, Fully Furnished=2,Semi-Furnished=1,Not Furnished=0")
    road = st.number_input("Main Road",placeholder="Enter if you want near main road,YES=1,No=0")
    guestroom = st.number_input("Guestroom",placeholder="Enter 1 if you need guestroom,enter 0 if you dont need guestroom")
    basement = st.number_input("Basement",placeholder="Enter 1 if you want basement,enter 0 if you dont want basement")
    hot_water = st.number_input("Hotwater Heating",placeholder="Enter 1 if you want hot water heater,enter 0 if you dont want hot water heater")
    pre_area = st.number_input("Preferred Area",placeholder="Enter 1 if you in preferred area, enter 0 if you dont need in pref area")
    air = st.number_input("Air Conditioning",placeholder="Enter 1 if you have air conditioning, enter 0 if you dont need air conditioning")
    
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
        
        if basement == 1:
            basement_no, basement_yes = 0,1
        else:
            basement_no, basement_yes = 1,0
        if road == 1:
            road_no, road_yes = 0,1 
        else:
            road_no , road_yes = 1,0
        if guestroom == 1:
            guestroom_no, guestroom_yes = 0,1
        else:
            guestroom_no, guestroom_yes = 1,0 
        if hot_water == 1:
            hot_water_no, hot_water_yes = 0,1
        else:
            hot_water_no, hot_water_yes = 1,0
        if air == 1:
            air_no, air_yes = 0,1
        else:
            air_no, air_yes = 1,0
        if pre_area == 1:
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