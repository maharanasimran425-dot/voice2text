from google import genai
import streamlit as st

st.title("Voice to Text")
client = genai.Client(api_key="AIzaSyDL6aRIsmiFyLxMsNY6Cvh34bcr_MTifrE")
file_name = st.file_uploader(
    "Upload an audio file",
    type=["wav", "mp3", "m4a"]
)
def audio(file_name):
    myfile = client.files.upload(file=file_name,
                                config={"mime_type": file_name.type}
)
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents=["""Describe the audio in short, Keep original language and accent
- Use correct punctuation
- Do not add explanations or extra text
-give a small heading about the topic""", myfile]
    )
    return response


if st.button("Generate"):
    if file_name:
        with st.spinner("Processing..."):
            result=audio(file_name)
            st.write(result.text)
    else:
        st.warning("Upload a file first")
