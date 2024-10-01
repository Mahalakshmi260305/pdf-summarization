# PROJECT NAME : PDF Summarization App

        This project is a web-based application that extracts text from PDF documents and generates concise summaries using a pre-trained BART model. It simplifies the task of reading lengthy documents by providing users with quick, accurate summaries.

# Features

        Automatic Text Extraction: Extracts text from uploaded PDF files.

        Summarization: Generates concise summaries of the extracted text using a pre-trained BART model. 

        User-Friendly Interface: Easy-to-use web app built with Streamlit for simple interaction.

        Custom Summarization: Fine-tuned BART model provides high-quality summaries.

# Installation
# prerequisites

Before running the app, ensure you have the following installed:

>>Python 3.7+
 **required python libraries
    >>streamlit
    >>PyMuPDF (fitz)
    >>transformers








#   Download and place the BART model:

    You need to download a pre-trained BART model from Hugging Face and place it in a folder, for example, C:\summary\New folder. Make sure that the folder paths in your code are correct.

# Usage

**Run the app:
        stream run app.py

**Upload a PDF:

    Open the local URL provided by Streamlit (usually http://localhost:8501).
    Upload a PDF file via the web interface.

**Extract and summarize text:

    After uploading, the app will extract text from the PDF.
    Click the Summarize button to generate a concise summary of the document.
