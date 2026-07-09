import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

for i, voice in enumerate(voices):
    print(f"Voice {i}")
    print("ID:", voice.id)
    print("Name:", voice.name)
    print("Language:", voice.languages)
    print("-" * 30)
    
    engine.setProperty("voice", voices[1].id)
    engine.say( "Hellooooooo    aaAvinash")
    engine.say("good by avinash")
    engine.runAndWait()