# import pyttsx3
# import speech_recognition as sr
# import webbrowser
# import datetime
# # Initialize text - to -speech
# engine = pyttsx3.init()

# def speak(text):
#     print("Assistant:", text)
#     engine.say(text)
#     engine.runAndWait()
    
# # take voice input
# def take_command():
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening...")
#         r.adjust_for_ambient_noise(source)
#         audio = r.listen(source)
#     try:
#         print("Recognizing...")
#         command = r.recognize_google(audio).lower()
#         print("You said:", command)
#     except Exception as e:
#         speak("Sorry, I didn't catch that. Please say it again.")
#         return ""
#     return command
# # function
# def open_youtube():
#     webbrowser.open("https://www.youtube.com")
#     speak("Opening Youtube")
# def open_google():
#     webbrowser.open("https://www.google.com")
#     speak("Opening google")
# def tell_time():
#     time = datetime.datetime.now().strftime("%I:%M %p")
#     speak(f"The current time is{time}")
# def tell_joke():
#     joke = "why do programmers perfer dark mode? because light attracts bugs!"
#     speak(joke)
# #
# def run_assistant():
#     speak("Hello, I am your assistant. how can i help you today?")
#     while True:
#         command = take_command()
        
#         if "open youtube" in command:
#             open_youtube()
#         elif "open google" in command:
#             open_google()
#         elif "tell me a joke" in command:
#             tell_joke()
#         elif "time" in command:
#             tell_time()
#         elif "exit" in command or "quit" in command:
#             speak("goodbye!")
#             break
#         elif command == "":
#             continue
        
#         else:
#             speak("Sorry, I don't understand that command")
            
# # run
# run_assistant()
            