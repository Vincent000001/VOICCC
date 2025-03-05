import speech_recognition as sr

def recognize_speech_from_audio(file_path):
    recognizer = sr.Recognizer()
    with sr.AudioFile(file_path) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        return f"Could not request results from Google Speech Recognition service; {e}"

if __name__ == "__main__":
    file_path = "path/to/audio/file.wav"
    recognized_text = recognize_speech_from_audio(file_path)
    print(f"Recognized Text: {recognized_text}")
