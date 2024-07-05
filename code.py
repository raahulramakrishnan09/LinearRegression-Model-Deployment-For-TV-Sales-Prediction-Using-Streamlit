import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
#load data
df=pd.read_csv('/content/tvmarketing.csv')

# Model training
model = joblib.load('/content/model.joblib')

st.title('Sales Prediction')
st.markdown('Enter the TV advertising budget to predict sales:')

tv_budget = st.number_input('TV Advertising Budget', min_value=0.0)

if st.button('Predict'):
    predicted_sales = model.predict([[tv_budget]])
    st.write(f'Predicted Sales: {predicted_sales[0]:.2f}')