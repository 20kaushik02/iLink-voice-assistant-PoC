from gtts import gTTS
from io import BytesIO

class TTSWrapper:
    def __init__(self, tts_model=gTTS):
        self.speech_model = tts_model
        
    def speak(self, text: str) -> BytesIO:
        output = BytesIO()
        self.speech_model(text).write_to_fp(output)
        return output