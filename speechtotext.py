import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Adjusting for background noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Listening... Please speak.")
        
        try:
    
            audio_data = recognizer.listen(source)
            
            print("Recognizing...")
            text = recognizer.recognize_google(audio_data)
            print("You said: ", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    speech_to_text()
