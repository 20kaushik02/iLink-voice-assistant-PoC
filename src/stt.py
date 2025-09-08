import whisper

small_en_model = whisper.load_model("small.en")

class STTWrapper:
    def __init__(self, trsc_model=small_en_model):
        self.transcription_model = trsc_model
    
    def transcribe(self, audio_input):
        return self.transcription_model.transcribe(audio_input, fp16=False)["text"]