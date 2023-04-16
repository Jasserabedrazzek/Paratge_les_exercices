import streamlit as st

# Upload file
uploaded_file = st.file_uploader("Choose a file")

# If file is uploaded
if uploaded_file is not None:
    # Get file content as bytes
    file_content = uploaded_file.read()
    # Display file content
    st.write(file_content)
    # Create download button
    st.download_button(
        label="Download file",
        data=file_content,
        file_name="uploaded_file.txt",
        mime="text/plain"
    )
