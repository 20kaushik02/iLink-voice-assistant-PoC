import numpy as np
import tempfile

import streamlit as st

from stt import STTWrapper
from tts import TTSWrapper
from llm import LLMWrapper

stt_fn = STTWrapper().transcribe
tts_fn = TTSWrapper().speak
llm_fn = LLMWrapper().prompt


def run():
    transcribed_input = None
    st.set_page_config(page_title="Voice Assistant PoC", layout="wide")
    st.write(
        """
    # Voice Assistant PoC
    """
    )
    input_col, output_col = st.columns([0.3, 0.7])

    with input_col:
        spoken_input = st.audio_input(
            "Click the microphone to start/stop recording", key="main-voice-input"
        )

        if spoken_input:
            st.write("Recorded input:")
            st.audio(spoken_input)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
                tmp.write(spoken_input.getbuffer())  # write the recorded bytes
                tmp_path = tmp.name
                transcribed_input = stt_fn(tmp_path)
            st.text_area(
                label="Transcribed input:",
                value=transcribed_input,
                disabled=True,
            )

    with output_col:
        if transcribed_input:
            #######################
            # text to LLM+RAG+etc.
            #######################
            transcribed_output = llm_fn(transcribed_input)

            st.text_area(
                label="Transcribed output:",
                value=transcribed_output,
                disabled=True,
                height="content",
            )

            spoken_output = tts_fn(transcribed_output)
            st.write("Text-to-speech:")
            st.audio(spoken_output, autoplay=True)


if __name__ == "__main__":
    run()
