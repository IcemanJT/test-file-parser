# Author: Jeremi Torój
# Date: 30/05/2024

import streamlit as st
import requests

FLASK_API_URL = 'http://127.0.0.1:5000'

st.title("File Upload and Processing App")
uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    files = {'file': (uploaded_file.name, uploaded_file.getvalue())}

    response = requests.post(f'{FLASK_API_URL}/upload', files=files)
    if response.status_code == 200:
        summary = response.json()
        st.write(summary)
    else:
        st.error(response.json().get('error', 'An error occurred'))

if 'display_metrics' not in st.session_state:
    st.session_state.display_metrics = False

if st.button('Fetch Metrics'):
    if st.session_state.display_metrics:
        st.session_state.display_metrics = False
    else:
        metrics_response = requests.get(f'{FLASK_API_URL}/metrics')
        if metrics_response.status_code == 200:
            st.text(metrics_response.text)
            st.session_state.display_metrics = True
        else:
            st.error('Failed to fetch metrics')
