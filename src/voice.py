from openai import OpenAI
import os

class SentinelVoice:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def transcribe_audio(self, audio_file_path):
        """Converts spoken commands into actionable audit text."""
        try:
            with open(audio_file_path, "rb") as audio_file:
                transcript = self.client.audio.transcriptions.create(
                    model="whisper-1", 
                    file=audio_file,
                    response_format="text"
                )
            return transcript
        except Exception as e:
            return f"Voice Error: {str(e)}"
