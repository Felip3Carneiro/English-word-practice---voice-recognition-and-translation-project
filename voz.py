import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import os

from googletrans import Translator

duration = 5
sample_rate = 44100

translator = Translator()

def falar(palavra):
    input("Aperte enter para poder falar...")
    print("Fale agora...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    # Salva o áudio
    wav.write("output.wav", sample_rate, recording)

    print("Gravação concluída! Reproduzindo...")

    # Reproduz o áudio gravado
    sd.play(recording, sample_rate)
    sd.wait()
    os.system('cls')

    print("Reprodução concluída, estou reconhecendo...")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio, language="en")

        translated1 = translator.translate(text, dest="en")
        fala = translated1.text

    except sr.UnknownValueError:
        print("A fala não pôde ser reconhecida.")
        fala = "Muito errado, tente falar melhor!"

    except sr.RequestError as e:
        print(f"Service error: {e}")
        fala = "Erro no serviço de reconhecimento."

    finally:
        translated2 = translator.translate(palavra, src="pt", dest="en")#src -> lingua original para ajudar a traduzir
        certo = translated2.text

        print("Você falou:", fala.capitalize())
        print("Deveria ser:", certo.capitalize())
        
        return fala.lower(), certo.lower()