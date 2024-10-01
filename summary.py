import streamlit as st
import fitz  
import os
from transformers import BartTokenizer, BartForConditionalGeneration


def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype='pdf') as doc:
        for page in doc:
            text += page.get_text()
    return text


def summarize_with_bart(text):
    tokenizer = BartTokenizer.from_pretrained(r'C:\summary\New folder')  
    model = BartForConditionalGeneration.from_pretrained(r'C:\summary\New folder') 

    inputs = tokenizer(text, return_tensors='pt', max_length=1024, truncation=True)
    summary_ids = model.generate(inputs['input_ids'], max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)


st.title("PDF Summarization App")
st.write("Upload a PDF file to get its summary:")


pdf_file = st.file_uploader("Choose a PDF file", type='pdf')


pdf_text = ""

if pdf_file is not None:
    
    pdf_text = extract_text_from_pdf(pdf_file)
    
    if pdf_text:
        st.subheader("Extracted Text:")
        st.write(pdf_text[:1000] + "...")  

        
        if st.button("Summarize"):
            summary = summarize_with_bart(pdf_text)
            st.subheader("Summary:")
            st.write(summary)
    else:
        st.warning("No text found in the PDF file.")
else:
    st.info("Please upload a PDF file to summarize.")
