import io
import streamlit as st
from docx import Document

import main

def stream():
    st.title("Legal Document Summarizer")
    uploaded_file = st.file_uploader("Upload a DOCX file", type=["docx"])
    #st.write(main.summarize(uploaded_file))
    if uploaded_file is not None:
        # Display the file details
        st.write("File Details:")
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
        st.write(file_details)

        # Display the content of the DOCX file
        if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            docx_content = uploaded_file.read()

            def process_document(docx_content):
                # Convert binary content to a BytesIO object
                docx_file = io.BytesIO(docx_content)

                # Create a docx.Document object
                doc = Document(docx_file)

                # Extract text from the document
                text = "\n".join([p.text for p in doc.paragraphs])

                return text

            # Send the document content to another class or function for processing
            processed_data=process_document(docx_content) # Call your processing function here
            st.write("File Content:")
            st.write(processed_data)
            text=main.summarize(processed_data)
            st.write("Processed Data:")
            st.write(text)
        else:
            st.write("File type not supported. Please upload a DOCX file.")

if __name__=="__main__":
    stream()