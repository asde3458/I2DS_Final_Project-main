import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

class ApartmentPricePredictor:
    def __init__(self, model_path):
        path = os.path.dirname(__file__)
        self.model = joblib.load(path + '/' + model_path)

    def predict_for_sale(self, data):
        return self.model.predict(data)

def main():
    st.title("Predict the price of renting and selling apartment in Ho Chi Minh City")
    st.subheader("Group 14")
    st.text("21120275 - Huynh Cao Khoi")
    st.text("21120308 - Pham Le Tu Nhi")

    st.header("Select some features")

    type = st.selectbox("**Type**", ('For sale', 'For rent'))
    if type == 'For sale':

        district_list = ['District 1',
                        'District 10', 'District 11', 'District 12', 'District 2', 'District 3',
                        'District 4', 'District 5', 'District 6', 'District 7', 'District 8',
                        'District 9', 'Bình Chánh District', 'Bình Thạnh District', 'Bình Tân District', 
                        'Gò Vấp District', 'Hóc Môn District','Nhà Bè District', 'Phú Nhuận District', 
                        'Thủ Đức District', 'Tân Bình District', 'Tân Phú District']
    else :

         district_list = ['District 1',
                        'District 10', 'District 11', 'District 12', 'District 2', 'District 3',
                        'District 4', 'District 5', 'District 6', 'District 7', 'District 8',
                        'District 9', 'Bình Chánh District', 'Bình Thạnh District', 'Bình Tân District', 'Củ Chi District',
                        'Gò Vấp District', 'Hóc Môn District','Nhà Bè District', 'Phú Nhuận District', 
                        'Thủ Đức District', 'Tân Bình District', 'Tân Phú District']

    
    selected_district = st.selectbox("**District**", tuple(district_list))
    area = st.slider('**Area(m2)**', 20, 250)
    bedroom = st.slider('**Bedroom(Phòng)**', 1, 6, 1)
    toilet = st.slider('**Toilet(Phòng)**', 1, 5, 1)

    input_data = {
        'Area': [area],
        'Bedroom': [bedroom],
        'Toilet': [toilet],
    }

    for district in district_list:
        input_data[district] = [1 if district == selected_district else 0]

    df = pd.DataFrame(input_data)


    if st.button('**Predict Price**'):
        if type == 'For sale':
            st.text('Predict price of apartment for sale')
            predictor = ApartmentPricePredictor('decision_tree_model_for_sale.sav')
            price = predictor.predict_for_sale(df.values)

            if price[0] < 0:
                st.text("Cannot predict the price")
            else:
                st.text("The predicted price for the apartment is {:,} (VND)".format(np.round(price[0], 2)*1000000))
        elif type == 'For rent':
            st.text('Predict price of apartment for rent')

            predictor = ApartmentPricePredictor('decision_tree_model_for_rent.sav')
            price = predictor.predict_for_sale(df.values)

            if price[0] < 0:
                st.text("Cannot predict the price")
            else:
                st.text("The predicted price for the apartment is {:,} (VND)".format(np.round(price[0], 2)*1000000))
       

if __name__ == "__main__":
    main()
