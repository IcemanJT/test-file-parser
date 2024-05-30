# streamlit_app.py
import streamlit as st
import requests

# Define the Flask endpoint
FLASK_API_URL = 'http://127.0.0.1:5000/upload'

# Streamlit app
st.title("File Upload and Processing App")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=['txt', 'csv', 'json'])

if uploaded_file is not None:
    print(uploaded_file.name)
    files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}

    response = requests.post(FLASK_API_URL, files=files)

    if response.status_code == 200:
        summary = response.json()
        st.write(summary)
    else:
        st.error(response.json().get('error', 'An error occurred'))
