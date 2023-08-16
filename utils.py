import speech_recognition as speech_r
from pydub import AudioSegment

def speech_to_text(path):
    # конвертирование файла .oga в .wav
    audio = AudioSegment.from_file(path, format="ogg")
    wav_path = path.replace(".oga", ".wav")
    audio.export(wav_path, format="wav")
    
    # распознавание речи
    sample = speech_r.AudioFile(wav_path)
    recognizer = speech_r.Recognizer()

    with sample as audio_file:
        recognizer.adjust_for_ambient_noise(audio_file)
        content = recognizer.record(audio_file)

        return recognizer.recognize_google(content, language="ru-RU")