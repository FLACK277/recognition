from gtts import gTTS
import os
import pyttsx3
text = 'Machine Learning (ML) is a subset of artificial intelligence (AI) that enables systems to learn from data and improve their performance without being explicitly programmed. It involves algorithms that identify patterns in data and make predictions or decisions based on that data.'
text_to_speech = pyttsx3.init()
text_to_speech.setProperty('rate', 150)
voices = text_to_speech.getProperty('voices')
text_to_speech.setProperty('voice', voices[0].id) 
text_to_speech.say(text)
text_to_speech.runAndWait()