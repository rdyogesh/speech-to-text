import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source, duration=2)
    print("say...")
    recordedaudio = recognizer.listen(source)
    print("done ")
    try:
        print("ur message .. ")
        text = recognizer.recognize_google(recordedaudio, language="en-US")
        print(text)
    except Exception as ex:
        print(ex)
