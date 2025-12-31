# app.py
import streamlit as st
from elevenlabs.client import ElevenLabs
from dotenv import load_dotenv
from io import BytesIO
import os
from langchain_core.messages import SystemMessage
from chat_feature import chat

load_dotenv()

st.title("🎤 AI Voice Enabled Assistant")

if "conversation" not in st.session_state:
    st.session_state.conversation = [
        SystemMessage(
            content=(
                "You are a helpful assistant. "
                "If information is missing, ask clarifying questions explicitly "
                "starting with 'ASSUMPTIONS:' and list them."
            )
        )
    ]

elevenlabs = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

audio_input = st.audio_input("Speak")

if audio_input:
    audio_bytes = BytesIO(audio_input.getbuffer())

    transcription = elevenlabs.speech_to_text.convert(
        file=audio_bytes,
        model_id="scribe_v1",
        language_code="eng"
    )

    user_text = transcription.text
    st.write("📝", user_text)

    remember = st.checkbox("Remember this conversation")

    response, updated_conversation = chat(
        user_text,
        st.session_state.conversation
    )

    content = response.content
    st.write("🤖", content)

    # Detect assumptions
    if content.startswith("ASSUMPTIONS:"):
        assumptions = content.replace("ASSUMPTIONS:", "").split("\n")
        clarifications = []

        st.subheader("Please clarify:")

        for a in assumptions:
            choice = st.radio(a, ["True", "False"], horizontal=True)
            clarifications.append(f"{a} is {choice}")

        if st.button("Submit clarifications"):
            clarification_text = " ".join(clarifications)
            response, updated_conversation = chat(
                clarification_text,
                st.session_state.conversation
            )
            st.write("🤖", response.content)

    else:
        audio_gen = elevenlabs.text_to_speech.convert(
            text=response.content,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2"
        )
        audio_out = b"".join(audio_gen)
        st.audio(audio_out, format="audio/mp3")

    if remember:
        st.session_state.conversation = updated_conversation
