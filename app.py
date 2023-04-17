import speech_recognition as sr


#use a prerecorded file to track speech recognition

filename = "speech.wav"

r = sr.Recognizer()

with sr.AudioFile(filename) as source:
    #load data to memory
    audio_data = r.record(source)
    #recognize
    text = r.recognize_google(audio_data)

    print(text)