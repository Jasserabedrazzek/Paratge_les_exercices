import streamlit as st
import json

# Define a function to serialize the uploaded file metadata to a JSON string
def serialize_file_metadata(file):
    return {
        "name": file.name,
        "type": file.type,
        "size": file.size,
    }

# Define the Streamlit app
def main():
    # Create a file uploader in the Streamlit app
    uploaded_file = st.file_uploader("Choose a file")

    # If a file has been uploaded, serialize its metadata and save it to a JSON file
    if uploaded_file is not None:
        metadata = serialize_file_metadata(uploaded_file)
        with open("uploaded_files.json", "a") as f:
            json.dump(metadata, f)
            f.write("\n")

        # Display the uploaded file's metadata
        st.write("Metadata:", metadata)

# Run the Streamlit app
if __name__ == "__main__":
    main()
