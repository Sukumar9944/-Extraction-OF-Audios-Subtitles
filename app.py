import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
import pandas as pd

# Setting Webpage Configurations
st.set_page_config(page_icon="🎶",page_title="Audio Extracter", layout="wide")

st.title(':blue[Audio Subtitle Extracter 🎧]')

audio_file_uploader = st.file_uploader("Upload a .WAV file")
submit = st.button('Extract')

# initialize the recognizer
recognizer = sr.Recognizer()

# Create a Translator object
translator = GoogleTranslator(source='ta', target='en')

# Audio file --> Audio Data --> Text

data = []

try:
    with st.spinner('Extracting...'):
        if audio_file_uploader and submit:
            audio_file = sr.AudioFile(audio_file_uploader)

            with audio_file as source:
                audio_data = recognizer.record(source)
                
            text = recognizer.recognize_google(audio_data, language = 'ta-IN')

            translated_text = translator.translate(text)

            data_dict = {'filename':audio_file_uploader.name,
                        'Tamil_subtitle': text,
                        'English_subtitle':translated_text}

            data.append(data_dict)

            new_df = pd.DataFrame(data = data)
            st.dataframe(new_df, width = 1200, hide_index = True)
            st.success('Info Extraxted Successfully')

except:
    st.warning('Please check your internet connection')