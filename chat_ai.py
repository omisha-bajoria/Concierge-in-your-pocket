"""This is a Personal AI Assistant to help with travelling."""


print("Code began.")        # Indicates that code execution has started.

import speech_recognition as sr
import openai
import pyttsx3
from my_openai_apikey import my_apikey
# import nltk

engine = pyttsx3.init()


def say(text):
    engine.say(text)
    engine.setProperty('rate',150)
    engine.runAndWait()



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source=source, duration=0.6)
        r.energy_threshold=300
        r.pause_threshold = 1
        print("Before listening...")
        audio = r.listen(source=source, timeout=5)
        print("After listening...")


        try:
            say("Recognizing...")
            query = r.recognize_google(audio_data=audio, language="en-in")
            query = query.lower()
            print(f"User: {query}")
            return query
        except sr.UnknownValueError:
            return "Sorry! I didn't catch that. Could you please repeat?"
        except sr.RequestError:
            return "There seems to be an issue with the speech recognition service. Please try again later."


    
def ai(prompt):
    openai.api_key = my_apikey

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    try:
        reply=response["choices"][0]["text"]
        print(f"Jarvis: {reply}")
        say(reply)
        # say(reply)
    except NameError:
        say("Sorry! Couldn't find anything related to your request.")


chatStr=""


def chat(query):
    global chatStr
    # print(chatStr)
    openai.api_key=my_apikey
    chatStr += f"User: {query}\nJarvis"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(f"{response['choices'][0]['text']}")
    say(text=response['choices'][0]['text'])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]





if __name__ == "__main__":
    say("Hello! I am Jarvis, your personal assistant for travelling. How may I help you?")
    query = input("Please tell me your requirements: ")

    while True:
        user_input = takeCommand()
        
        if user_input.lower() == 'exit':
            print("Jarvis: Goodbye!")
            break

        ai(prompt=user_input)










    print("Code over.")


# Please note that to use this, you need an ACTIVE INTERNET CONNECTION. Else it won't work.
