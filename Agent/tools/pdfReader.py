from langchain_core.tools import tool
import pypdf
import os
@tool
def pdfReader(fileLocation:str):
    """This tool will help to extract the test from pdf"""
    print("Received:", fileLocation)

    if not os.path.exists(fileLocation):
        return f"File does not exist: {fileLocation}"

    reader = pypdf.PdfReader(fileLocation)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text

    return text