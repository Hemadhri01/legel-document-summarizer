from docx import Document


def reader(fileurl):
    doc = Document(fileurl)  # Replace 'document.docx' with the path to your Word document

    # Initialize an empty string to store the extracted text
    extracted_text = ""

# Iterate through the paragraphs in the document and append their text to the result
    for paragraph in doc.paragraphs:
        extracted_text += paragraph.text + "\n"

# Print or manipulate the extracted text
    #print(extracted_text)
    return extracted_text



