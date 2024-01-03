"""This is a Personal Desktop AI Assistant."""


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
        audio = r.listen(source=source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio_data=audio, language="en-in")
            query = query.lower()
            print(f"User: {query}")
            return query
        except Exception:
            return "Some error occurred!!! Apologies from Jarvis "


    
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
    except UndefinedVariableError:
        print("Jarvis: Sorry! Couldn't find anything related to your request.")


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
    print(f"Jarvis: {response['choices'][0]['text']}")
    say(text=response['choices'][0]['text'])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]





if __name__ == "__main__":
    print("Jarvis: Hello! I am Jarvis, your personal desktop assistant. How may I help you?")
    # query = input("Jarvis: ")
    # say(text="Hello! I am Jarvis, your personal desktop assistant. How may I help you?")
    
    # if "using artificial intelligence" in query or "using ai" in query:
    ai(prompt=query)

    # chat(query=query)

    # say(text=f"User: {query}")










    print("Code over.")


# Please note that to use this, you need an ACTIVE INTERNET CONNECTION. Else it won't work.