import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter

#Upload PDF Files
st.header("My First ChatBot")

with st.sidebar:
    st.title("ARD-ChatBot")
    file = st.file_uploader("Upload a PDF file and start asking question", type="pdf")

#Extract the test
if file is not None:
    pdf_reader = PdfReader(file)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
        #st.write(text)

#Break it into chunks
    test_splitter = RecursiveCharacterTextSplitter(
        seprators="\n",
        chunk_size=100,
        chunk_overlap=150,
        length_function=len
    )
    chunks = text_splitter.split_text(test)
    st.write(chunks)
    

