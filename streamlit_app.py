import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("API_KEY"))
system_prompt = """
    You are a translator. translate what the user pass in into the language they chose. Just return the translated text,nothing else.
"""
user_prompt = ""

"""
# Translator
This translates text
"""

translated_text = ""

with st.form("my_form"):
    languages = ["English","Chinese","Vietnamese","French"]
    input_lang = st.selectbox("Please select an input language",languages)
    output_lang = st.selectbox("Please select an output language",languages)
    text = st.text_area("Enter text that is being translated:")
    user_prompt = "Translate " + text + " from " + input_lang + " to " + output_lang
    submit = st.form_submit_button("Translate")

    if submit:
        translated_text = client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages = [
                {"role":"system","content": system_prompt},
                {"role":"user","content": user_prompt},


            ]
            

        )

if translated_text:
    st.write(translated_text.choices[0].message.content)



    
