import os
import streamlit as st
from pypdf import PdfReader
from groq import Groq

@st.cache_data
def extract_pdf_text(pdf_path: str) -> str:
    """
    Extracts unstructured textual data from standard operating procedures 
    (SOPs) or factory manuals to serve as knowledge context for RAG.
    """
    if not os.path.exists(pdf_path):
        return "Standard safety protocols apply. No specific document found."
    
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text[:4000]  # Safe token threshold for context windows
    except Exception as e:
        return f"Error reading PDF: {str(e)}"

def execute_cognitive_inference(client: Groq, prompt: str, context: str = "") -> str:
    """
    Executes a high-performance factual inference query against Llama 3.3 (70B)
    using Groq's Ultra-Low Latency Language Processing Units (LPUs).
    """
    if not client:
        return "⚠️ system: Connection pipeline is inactive. Please provide a valid Groq API Key in the sidebar input box to run AI-powered modules."
        
    system_prompt = (
        "You are the central proprietary operating engine of PlantBrain. "
        "Provide a direct, engineering-grade response using the internal knowledge matrix. "
        "NEVER say phrases like 'Based on the provided context', 'According to the document', or 'As an AI'. "
        "Present the data directly as facts. "
        "At the very bottom of your response, create a clean line that says '📂 Reference Assets:' followed by the document citations."
    )
    
    full_prompt = f"Context from Plant Documents:\n{context}\n\nUser Query: {prompt}"
    
    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile", 
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.2, # Kept low to ensure deterministic engineering outcomes
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to Groq API: {str(e)}"