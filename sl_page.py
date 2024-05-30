# Author: Jeremi Torój
# Date: 30/05/2024

import streamlit as st
import requests

FLASK_API_URL = 'http://127.0.0.1:5000/upload'

st.title("File Upload and Processing App")

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    files = {'file': (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}

    response = requests.post(FLASK_API_URL, files=files)

    if response.status_code == 200:
        summary = response.json()
        st.write(summary)
    else:
        st.error(response.json().get('error', 'An error occurred'))
