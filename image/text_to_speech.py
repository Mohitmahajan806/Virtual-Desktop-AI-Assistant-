import pyttsx3

text="geeksforgeeks"
engine=pyttsx3.init()
rate=engine.getProperty('rate')
engine.setProperty('rate','rate-70')
engine.say(text)
engine.runAndWait()
