"""This is a Personal AI Assistant to help with traveling."""


print("Code began.")        # Indicates that code execution has started.

import speech_recognition as sr
import openai
import pyttsx3
from my_openai_apikey import my_apikey
import pyaudio
# import nltk


engine = pyttsx3.init()
# print("Started")


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
        # print("Before listening...")
        audio = r.listen(source=source, timeout=5)
        # print("After listening...")


        try:
            say("Recognizing...")
            query = r.recognize_google(audio_data=audio, language="en-in")
            query = query.lower()
            print(f"User: {query}")
            # chatStr += f"User: {query}\n"
            return query
        except sr.UnknownValueError:
            return "Sorry! I didn't catch that. Could you please repeat?"
        except sr.RequestError:
            return "There seems to be an issue with the speech recognition service. Please try again later."


    
def ai(prompt):
    openai.api_key = my_apikey

    response = openai.completions.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    

    try:
        # reply=response["choices"][0]["text"]
        reply = response.choices[0].text
        print(f"Jarvis: {reply}")
        # say(reply)
        chatStr += f"Concierge: {reply}\n"
        # say(reply)
    except NameError:
        say("Sorry! Couldn't find anything related to your request.")


chatStr=""


def chat(query1):
    global chatStr
    # print(chatStr)
    query = input(f"User: ")
    openai.api_key=my_apikey
    # chatStr += f"User: {query}\nJarvis"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=0.7,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(f"Concierge: {response['choices'][0]['text']}")
    # say(text=response['choices'][0]['text'])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]





if __name__ == "__main__":
    temp_used_str = "Hello! This is Concierge in Your Pocket, your personal assistant for travelling. How may I help you?"
    say(f"{temp_used_str}")
    # query = input("Please tell me your requirements: ")
    print("Please tell me your requirements: ")
    # chatStr += f"Concierge: {temp_used_str}\n"

    while True:
        print("listening")
        user_input = takeCommand()
        
        if user_input.lower() == 'exit':
            print("Jarvis: Goodbye!")
            break

        ai(prompt=user_input)
        # chat(query=user_input)










    print("Code over.")


# Please note that to use this, you need an ACTIVE INTERNET CONNECTION. Else it won't work.
