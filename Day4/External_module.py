import pyttsx3

engine = pyttsx3.init()

engine.say("Hello Avinash You successfully installed the pyttsx3 that is external module")

engine.setProperty("rate", 150)
engine.setProperty("volume",1.0)

voices = engine.getProperty("voices")
print(voices)

engine.runAndWait()