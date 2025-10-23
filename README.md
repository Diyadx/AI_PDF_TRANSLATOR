# AI_PDF_TRANSLATOR


A smart AI-powered tool that converts scanned PDF files into readable, translatable, and audible text using OCR (PyTesseract), LangChain, and Streamlit.

🌐 Live Demo: Streamlit App

💻 Tech Stack: Python, PyTesseract, LangChain, Streamlit, gTTS, PDF2Image

🚀 Features

📄 OCR Extraction: Extracts text from scanned PDFs using PyTesseract and Poppler.

🌍 AI Translation: Uses LangChain with Groq/Google models to translate text into multiple languages with 85%+ accuracy.

🔊 Text-to-Speech: Converts translated text into audio using gTTS for better accessibility.

🧠 AI Spell Correction: Automatically corrects extracted text using TextBlob.

💾 Downloadable Output: Generates a downloadable .txt file of the translated text using Base64 encoding.

🧰 Streamlit Web UI: Simple, user-friendly interface that allows real-time translation and audio playback.

🧩 Tech Stack

Python 3.9+

Streamlit – Web app interface

PyTesseract – OCR text extraction

LangChain – AI translation pipeline

Groq / Google GenAI – Language model APIs

TextBlob – Spell checking

gTTS – Text-to-speech conversion

pdf2image & Poppler – PDF page rendering
