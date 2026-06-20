# Smile - Your AI-Powered Voice Assistant
#### Video Demo: [Click here to watch the demo](<https://youtu.be/i92gUElE-hc>)

#### Description:
Smile is an advanced voice assistant developed using Python, integrated with Google's Generative AI (`gemini-1.5-flash`), speech recognition capabilities, and real-time text-to-speech synthesis. Designed to streamline user interactions through voice commands, Smile can handle a variety of tasks, from providing motivational quotes to interpreting mathematical expressions.

Smile is built with accessibility in mind. Whether you're a student needing quick math solutions, a programmer looking for coding advice, or someone seeking inspiration through famous quotes, Smile has got you covered. The assistant listens to your commands, processes them using cutting-edge AI, and delivers spoken responses with a human-like quality.

#### Features:
- **Real-time Speech Recognition**: Smile uses Google’s Speech API for accurate and quick voice-to-text conversion.
- **Generative AI for Natural Conversations**: Powered by the `gemini-1.5-flash` model, Smile generates insightful, human-like responses.
- **Text-to-Speech Integration**: Using `pyttsx3`, Smile responds to your queries in a natural, articulate manner.
- **Dynamic Mathematical Expression Interpretation**: Smile can interpret and articulate mathematical symbols and equations.
- **Emoji Support**: Adds a fun, interactive layer to the conversation by displaying emojis that match the context.

#### Files Overview:
- **`finalproject.py`**: This is the main script for the project. It includes:
  - A `greeting()` function that tailors responses based on the time of day.
  - The `listen()` function, which uses the Google Speech API to capture user input via the microphone.
  - The `getquote()` function, which fetches and displays a random quote using the Quotable API.
  - The `mrsmyle()` function, which initiates a conversational session using Google’s Generative AI for chat responses.
  - Several utility functions like `speak()`, which converts text to speech, and `printer()`, which formats text outputs in the terminal.

- **`requirements.txt`**: This file contains a list of required libraries and dependencies, ensuring that the project can be set up easily in any Python environment. Dependencies include:
  - `pyttsx3` for text-to-speech conversion.
  - `speech_recognition` for capturing and interpreting voice input.
  - `google-generativeai` for AI-powered conversation capabilities.
  - `requests` for interacting with the Quotable API.

#### Design Decisions:
During the development of Smile, several design choices were carefully considered:
- **Choosing the Generative AI Model**: After testing multiple models, I chose Google’s `gemini-1.5-flash` for its balance of speed, accuracy, and response quality. It allowed for a conversational experience that felt natural, while keeping the responses concise.
- **Handling Mathematical Expressions**: Interpreting and speaking mathematical expressions was a challenging design task. The solution involved creating a custom function that converts mathematical notation (like superscripts and fractions) into readable text, ensuring that Smile could cater to technical users.
- **Text-to-Speech Engine**: I chose `pyttsx3` over other options like PyAudio due to its ease of setup and flexibility with different voices, rates, and languages. This choice also allowed Smile to be used on multiple platforms without additional audio dependencies.
- **User Interaction**: Smile includes emoji-based prompts and responses to make the interaction more engaging and visually appealing.

#### How to Run the Project:
1. Install the necessary dependencies from `requirements.txt` using:
