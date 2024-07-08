# Linear Regression Model Deployment Using Streamlit for TV Sales Prediction
This repository demonstrates how to deploy a Linear Regression algorithm model using Streamlit for predicting sales based on advertising budget.
## What is Streamlit?

Streamlit lets you transform Python scripts into interactive web apps in minutes, instead of weeks. Build dashboards, generate reports, or create chat apps. Once you’ve created an app, you can use our [Community Cloud platform](https://streamlit.io/cloud) to deploy, manage, and share your app.

### Why choose Streamlit?

- **Simple and Pythonic:** Write beautiful, easy-to-read code.
- **Fast, interactive prototyping:** Let others interact with your data and provide feedback quickly.
- **Live editing:** See your app update instantly as you edit your script.
- **Open-source and free:** Join a vibrant community and contribute to Streamlit's future.

## Streamlit Installation

Installs Streamlit, a Python library for creating web apps:

```python
!pip install streamlit -q
```

You're all set! If not, head over to [docs](https://docs.streamlit.io/get-started) for specific installs.


## Fetch Public IP Address
Retrieves your public IPv4 address using a web service:
```python
!wget -q -O - ipv4.icanhazip.com
```
## Writing to code.py
Creates or overwrites code.py with the subsequent commands:
```python
%%writefile code.py
```

## Install localtunnel:
This line uses npm to install localtunnel, which is used for exposing local servers to the internet:
```python
!npm install localtunnel
```
##Localtunnel Setup:
Installs localtunnel, starts the Streamlit app (code.py), and sets up a tunnel to expose it publicly:
```python
!streamlit run code.py & npx localtunnel --port 8501
```

# Files:
### model.joblib:
joblilb formatted machine learning model trained on the TV marketing dataset.

### code.py:
Python script containing streamlit web application code for model deployment.
```python
import streamlit as st
import pandas as pd
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
```
# Requirements:
- [Python](https://github.com/python)

- [Jupyter](https://github.com/jupyter)

- [Streamlit](https://github.com/streamlit)

- [Tensorflow](https://github.com/tensorflow)

- [keras](https://github.com/keras)

- [scikit-learn](https://github.com/scikit-learn)

- [numpy](https://github.com/numpy)


## License

Streamlit is completely free and open-source and licensed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.
