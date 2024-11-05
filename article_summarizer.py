from newspaper import Article
import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv
from fpdf import FPDF
import tempfile
import io
import re

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel("gemini-pro")

def extract_text_from_article(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text


def summarize(transcript,prompt):
    response=model.generate_content(prompt+transcript)
    return response.text

def create_pdf(transcript):
    # Create a PDF object
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    # Add the transcript text to the PDF
    pdf.multi_cell(0, 10, transcript)
    
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
        pdf.output(tmp_file.name, 'F')  # Save the PDF to a temporary file
        
        # Read the temporary file into BytesIO
        pdf_output = io.BytesIO()
        with open(tmp_file.name, 'rb') as f:
            pdf_output.write(f.read())
        
    # Clean up: Delete the temporary file
    os.remove(tmp_file.name)
    
    pdf_output.seek(0)  # Move to the beginning of the BytesIO buffer
    return pdf_output

st.title("Articles SUMMARIZER")
article_link=st.text_input("enter the article link")
summary_type=st.selectbox("select summary type",["paragraph summary","bullet point summary"])
summary_length=st.slider("select summary length in words",min_value=100, max_value=1000)

prompt=f"""Asuume you are the best text summarizer over 10 years experience .you need to provide summarize the
article transcript and return important article content as
{summary_type} in {summary_length} words.if possible bold the important words and sentences . here is my transcript:"""

a=st.button("Generate ")
if a:
    transcript=extract_text_from_article(article_link)
    st.markdown("##summary")
    summary=summarize(transcript,prompt)
    st.write(summary)
    summary = summary.encode('latin-1', 'replace').decode('latin-1')
    pdf_file = create_pdf(summary)
    summary.replace("–","")
    st.download_button(
        label="Download PDF",
        data=pdf_file,
        file_name="transcript.pdf",
        mime="application/pdf"
    )
