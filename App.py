#importing Necessary Libraries

import numpy as np
import pandas as pd
import pickle as pkl 
import streamlit as st
from PIL import Image



model = pkl.load(open('MIPML.pkl', 'rb'))
st.set_page_config(page_title="Your AI Assistant", page_icon="🖖")

logo = Image.open(r"STW-LOGO.png")
# st.image(logo)
col1, col2, col3 = st.columns(3)
with col1:
    st.write("")
with col2:
    st.image(logo, caption='STW Services')

with col3:
    st.write("")
st.header(':green[Medical Insurance Premium Predictor]',divider='blue')

gender = st.selectbox('Choose Gender',['Female','Male'])
smoker = st.selectbox('Are you a smoker ?',['Yes','No'])
region = st.selectbox('Choose Region', ['SouthEast','SouthWest','NorthEast','NorthWest'])
age = st.slider('Enter Age', 5 , 80)
bmi = st.slider('Enter BMI', 5 , 100)
children = st.slider('Choose No of Childrens', 0, 5)


if st.button('Predict'):
    if gender == 'Female':
     gender = 0
    else:
        gender = 1

    if smoker == 'Yes':
        smoker = 1
    elif smoker == 'No':
        smoker = 0
    if region == 'SouthEast':
        region = 0
    if region == 'SouthWest':
        region = 1
    if region == 'NorthEast':
        region = 2
    else:
        region = 3

    input_data = (age, gender, bmi, children,smoker, region)
    input_data_array = np.asarray(input_data)
    input_data_array = input_data_array.reshape(1,-1)
    predicted_prem = model.predict(input_data_array)

    display_string = 'Insurance Premium will be ₹ '+ str(round(predicted_prem[0],2)) 

    st.markdown(display_string)

