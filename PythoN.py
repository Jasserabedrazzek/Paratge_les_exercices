import streamlit as st
import json

# Create a form for file upload
with st.form("File Upload"):
    uploaded_file = st.file_uploader("Choose a file")

    # Add a submit button
    submit_button = st.form_submit_button(label='Submit')

# When the form is submitted
if submit_button and uploaded_file is not None:
    # Read the contents of the file
    file_contents = uploaded_file.read()

    # Process the file contents and create a JSON object
    json_data = {'file_name': uploaded_file.name, 'file_data': file_contents.decode('utf-8')}

    # Save the JSON object to a file
    with open('file_data.json', 'w') as f:
        json.dump(json_data, f)

    # Display the JSON data in the Streamlit app
    st.write('JSON Data:', json_data)
