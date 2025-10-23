import pytesseract
from PIL import Image
from pdf2image import convert_from_bytes
import streamlit as st
import base64
import io
from gtts import gTTS
from langchain_groq import ChatGroq
from textblob import TextBlob
import PyPDF2


st.title("AI-PDF Summarizer & Translator with Voice")
st.caption("Upload a PDF → Extract text → Summarize → Translate → Listen & Download")


if st.button("Clear Cache"):
    st.cache_data.clear()
    st.success("Cache cleared successfully!")


uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
target_lang = st.text_input("Enter target translation language (e.g. Hindi, French, Spanish):")
api_key = st.text_input("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", type="password")


def pdf_to_text(pdf_bytes):
    """Extract text from PDF pages using OCR."""
    all_text = ""
    for image in convert_from_bytes(pdf_bytes):
        text = pytesseract.image_to_string(image)
        all_text += text + "\n"
    return all_text

def correct_spelling(text):
    """Basic spell-check using TextBlob."""
    try:
        return str(TextBlob(text).correct())
    except:
        return text

def ai_summarize_and_translate(text, lang, api_key):
    """Use Groq LLM to summarize and translate text."""
    llm = ChatGroq(model="llama3-70b-8192", temperature=0.2, api_key=api_key)
    prompt = f"""
    Summarize the following text clearly, then translate it to {lang}:
    ```
    {text[:4000]}
    ```
    """
    result = llm.invoke(prompt)
    return result.content

def text_to_speech(text, lang_code="en"):
    """Convert text to speech and return audio bytes."""
    tts = gTTS(text=text, lang="en")
    audio_bytes = io.BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes.read()

def download_link(text, filename):
    """Create a base64 download link."""
    b64 = base64.b64encode(text.encode()).decode()
    href = f'<a href="data:text/plain;base64,{b64}" download="{filename}">📥 Download text file</a>'
    return href


if uploaded_file and target_lang and api_key and st.button("Process PDF"):
    pdf_bytes = uploaded_file.read()
    with st.spinner("Extracting text from PDF..."):
        extracted_text = pdf_to_text(pdf_bytes)
        extracted_text = correct_spelling(extracted_text)
    st.success("Text extraction complete ✅")

    with st.spinner("Summarizing and translating with AI..."):
        translated_summary = ai_summarize_and_translate(extracted_text, target_lang, api_key)
    st.success("Translation complete ✅")

    st.subheader("🔍 Translated Summary")
    st.markdown(translated_summary)

    
    st.audio(text_to_speech(translated_summary))

  
    st.markdown(download_link(translated_summary, "summary_translation.txt"), unsafe_allow_html=True)
