import streamlit as st

def main():
    st.title("House Price Predictor")
    
    # Input Fields
    area = st.number_input("Area", min_value=1,step=1,placeholder="Enter Area of House")
    beds = st.number_input("Bedrooms",min_value=1,step=1,placeholder="Enter no. of bedrooms")
    baths = st.number_input("Bathroom",min_value=1,step=1,placeholder="Enter no. of bathrooms")
    stories = st.number_input("Stories",min_value=1,step=1,placeholder="Enter no. of stories")
    parking = st.number_input("Parking",min_value=1,step=1,placeholder="Enter no.of parking space")

    Furnishing_Status = ['Furnished','Unfurnished','Semi-Furnished']
    Main_Road = ['Yes', 'No']
    Guestroom = ['Yes', 'No']
    Basement = ['Yes', 'No']
    Hotwater_Heating = ['Yes', 'No']
    Airconditioning=['Yes','No']
    Preferred_Area = ['Yes', 'No']
    furnish_map = {
        "Furnished": 0,
        "Unfurnished": 2,
        "Semi-Furnished": 1
    }

    house_furnishing_status = st.radio(label="House Furnishing Status", options=Furnishing_Status)
    user_main_road = st.radio(label="Select if you need the house near the main road", options=Main_Road)
    user_guestroom = st.radio(label="Do you need a guestroom?", options=Guestroom)
    user_basement = st.radio(label="Do you need a basement?", options=Basement)
    user_hotwater_heating = st.radio(label="Do you want hot water heating?", options=Hotwater_Heating)
    user_preferred_area = st.radio(label="Do you want the house in a preferred area?", options= Preferred_Area)
    air = st.radio(label="Do you want the house to have air conditioning?", options= Airconditioning)
    
    if  st.button("Submit"):
        import os
        import joblib
        import numpy as np
        
        ml_path = "app/pages/LinearModel.joblib"
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
        furnish = furnish_map[house_furnishing_status]
        
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
if __name__ == "__main__":
    main()