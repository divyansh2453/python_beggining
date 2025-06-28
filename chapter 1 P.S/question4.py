import pyttsx3

engine = pyttsx3.init()

# Set voice (male/female)
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")  # Show available voices

engine.setProperty('voice', voices[0].id)  # You can change 0 to 1 to try a different voice

# Set volume and speed
engine.setProperty('volume', 1.0)   # Max volume
engine.setProperty('rate', 150)     # Normal speaking rate

engine.say("it's done")
engine.runAndWait()
