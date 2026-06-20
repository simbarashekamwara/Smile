import datetime
import pyttsx3
import speech_recognition as sr
import sys
import time
import requests
import emoji
import google.generativeai as genai
import os
import re


#This function will print a greeting according to the time and Introduce itself.
def greeting(hour):

    if hour<12:
        return("Good morning")
    elif hour<18:
        return("Good afternoon")
    else:
        return("Good evening")

#this function will speak the text passed i.e provides voice output
def speak(text):

    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()


def _time():
    return datetime.datetime.now().time()


#This function listens to the user
def listen():

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:

            printer(f"Listening{emoji.emojize(':ear:', language='alias')}....")
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            return text


        except sr.UnknownValueError:
            speak("I'm listening… please give me your command")


        except sr.RequestError as e:
            speak("Could not request results from Google Speech Recognition service; {0}".format(e))







def getquote():

    response = requests.get("https://api.quotable.io/random")
    quote = response.json()
    return (f'"{quote['content']} — {quote['author']}"')



def printer(text):
        print(f"\033[3m{text}\033[0m")


import re

# Dictionary for special superscripts
special_superscripts = {
    '²': ' squared',
    '³': ' cubed',
    '⁰': ' to the power 0',
    '¹': ' to the power 1',
    '⁴': ' to the power 4',
    '⁵': ' to the power 5',
    '⁶': ' to the power 6',
    '⁷': ' to the power 7',
    '⁸': ' to the power 8',
    '⁹': ' to the power 9',
}

# Function to replace mathematical expressions
def replace_math_expressions(text):
    # Replace special superscripts
    for sup, replacement in special_superscripts.items():
        text = text.replace(sup, replacement)

    # Replace general superscripts (letters)
    text = re.sub(r'([a-zA-Z])\^([a-zA-Z0-9])', r'\1 to the power \2', text)

    # Replace function notation like f(x) with "f of x"
    text = re.sub(r'([a-zA-Z]+)\(([^)]+)\)', r'\1 of \2', text)

    # Handle Taylor series, e.g., f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)²/2! + ...
    text = re.sub(r'([a-zA-Z]+)\(([^)]+)\)\s*=\s*([^\.]+)\s*\.\.\.', r'\1 of \2 equals \3 and so on', text)

    # Handle summation notation, e.g., Σ (from k=0 to n) of f(k)
    text = re.sub(r'Sigma\s*\(\s*([a-zA-Z]+)\s*=\s*([0-9]+)\s*to\s*([0-9]+)\)\s*of\s*([a-zA-Z]+\([^)]+\))', r'the sum from \2 to \3 of \4', text)

    # Handle integrals, e.g., ∫ f(x) dx
    text = re.sub(r'∫\s*([a-zA-Z]+\([^)]+\))\s*dx', r'the integral of \1 with respect to x', text)

    # Replace square roots, e.g., sqrt(x) to "the square root of x"
    text = re.sub(r'sqrt\(([^)]+)\)', r'the square root of \1', text)

    # Replace fractions like a/b to "a over b"
    text = re.sub(r'([a-zA-Z0-9]+)\s*/\s*([a-zA-Z0-9]+)', r'\1 over \2', text)

    # Handle powers with letter bases, e.g., a^n as "a to the power n"
    text = re.sub(r'([a-zA-Z])\^([a-zA-Z0-9])', r'\1 to the power \2', text)

    # Handle logarithms, e.g., log(x) as "the logarithm of x"
    text = re.sub(r'log\(([^)]+)\)', r'the logarithm of \1', text)

    # Handle exponents, e.g., e^(x) as "e to the power x"
    text = re.sub(r'e\^\(([^)]+)\)', r'e to the power \1', text)

    return text



def mrsmyle(testing=False, mock_user_input=None):
    # Configure the model with the API key
    genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

    # Initialize the generative model and chat session
    model = genai.GenerativeModel("gemini-1.5-flash",  generation_config=genai.GenerationConfig(
        max_output_tokens=2000,
        temperature=0.2,))
    chat = model.start_chat(
        history=[
            {"role": "user", "parts": "Hello"},
            {"role": "model", "parts": "Great to meet you. What would you like to know?"},
        ]
    )

    # Loop to allow continuous user input

    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Loop to allow continuous user input via voice
    while not testing:
        try:
            # Capture voice input
            with sr.Microphone() as source:
                printer(f"Listening for your voice input{emoji.emojize(':ear:', language='alias')}...")
                audio = recognizer.listen(source)

            # Convert voice input to text
            user_input = mock_user_input if mock_user_input else  recognizer.recognize_google(audio)
            print(f"User: {user_input}")

            # If user wants to exit, break the loop
            if user_input.lower() in ["exit", "quit"]:
                print("Conversation ended.")
                break

            # Send the message to the chatbot (assuming chat is defined elsewhere)
            response = chat.send_message(user_input)

            # Print the chatbot's response
            plain_response = response.text.replace('*', '')
            plain_txt=plain_response.replace('#', '')

            plain_text=replace_math_expressions(plain_txt)
            print("Smile:", plain_txt)
            speak(plain_text)

            # Speak the chatbot's response (assuming speak function is defined)


        except sr.UnknownValueError:
            print("Sorry, I didn't understand that. Please try again.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        except KeyboardInterrupt:
            break



#this is the main function:
def main(testing=False, mock_request=None):

    #printer(getquote())

    greet=greeting(_time().hour)
    printer(f"Speaking{emoji.emojize(':microphone:', language='alias')}....")
    speak(f"{greet}! I'm Smile, here to help you with anything you need.Just say the word, and I'll be ready to assist. How can I help you today?")

    while not testing:
        request = mock_request if mock_request else listen()
        request=request.lower().strip()


        if 'exit' in request or 'stop' in request or 'quit' in request:

            speak("Catch you later! Stay awesome")
            time.sleep(2)
            sys.exit()
        elif 'who are you' in request:
            speak("I'm Smile, a Voice Assistant designed to help with a wide range of questions. Whether you need advice on programming, cybersecurity, or anything else, I'm here to assist you! How can I help you today?")

        elif 'current time' in request:
            print(f"{_time().hour}:{_time().minute}")
            speak(f"{_time().hour} {_time().minute}")

        else:
            print("Intiating conversation with Mr Smile.....")
            mrsmyle()


if __name__ == "__main__":
    main()
