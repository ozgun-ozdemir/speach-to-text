import speech_recognition as sr

# r=recognizer
r = sr.Recognizer()

print("Welcome!")

while True:
    try:
        with sr.Microphone() as m:
            r.adjust_for_ambient_noise(m, duration=1)
            print("Listening...")
            audio = r.listen(m)
 
            user_input = r.recognize_google(audio)
        
            print(f"You:  {user_input}")

        if user_input in ("exit", "bye", "stop", "finish", "quit"):  
            print("Goodbye!")
            break

    except sr.UnknownValueError:
        print("Please try again.")
        
