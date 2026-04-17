import pyttsx3

engine = pyttsx3.init()
# name = input("What your good name:")
# message = f"Hello {name} , I am Jarvis, Your personal assistant. How can I help you ?"
# print(message)

# engine.say(message)
# engine.runAndWait()

with open("xyz.txt","r") as file:
    message = file.read()
    
engine.say(message)
engine.runAndWait()
