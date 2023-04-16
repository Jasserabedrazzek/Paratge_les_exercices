import streamlit as st
import requests

# Create a file uploader widget
file = st.file_uploader("Upload a file", type=["txt", "pdf", "png", "jpg"])

# Check if a file has been uploaded
if file is not None:
    # Display the file details
    st.write("File details:")
    st.write(file.name)
    st.write(file.type)
    st.write(file.size)
    
    # Send the file to the server
    url = "http://example.com/upload"
    files = {"file": file.getvalue()}
    response = requests.post(url, files=files)
    
    # Display the response from the server
    st.write("Server response:")
    st.write(response.text)
