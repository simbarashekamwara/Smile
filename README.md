# Smile 🎙️
> An AI-powered voice assistant built in Python — talk to it, and it talks back.

![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Python](https://img.shields.io/badge/python-3.x-blue)
![AI](https://img.shields.io/badge/AI-Gemini%201.5%20Flash-orange)

🎬 **[Watch the Demo](https://youtu.be/i92gUElE-hc)**

---

## What is Smile?

Smile is a voice assistant that listens to what you say, thinks using Google's Gemini AI, and responds out loud — all from your terminal. No typing needed.

It handles natural conversation, answers questions, solves math expressions, fetches motivational quotes, and more — powered by real AI, not hardcoded responses.

---

## Features

- 🎤 **Voice Recognition** — Captures your voice in real time via Google's Speech API
- 🤖 **AI Conversations** — Powered by `gemini-1.5-flash` for natural, context-aware replies
- 🔊 **Text-to-Speech** — Speaks responses back using `pyttsx3`
- 🧮 **Math Expression Interpreter** — Reads out equations and symbols in plain English
- 💬 **Motivational Quotes** — Fetches random quotes from the Quotable API
- 😊 **Emoji Responses** — Displays context-matched emojis for a more engaging experience
- 🌅 **Time-aware Greetings** — Says good morning, afternoon, or evening based on the time

---

## Installation

```bash
git clone https://github.com/yourusername/Smile.git
cd Smile
pip install -r requirements.txt
python finalproject.py
```

### Dependencies

| Library | Purpose |
|---------|---------|
| `pyttsx3` | Text-to-speech engine |
| `speech_recognition` | Voice input via microphone |
| `google-generativeai` | Gemini AI conversation |
| `requests` | Fetch quotes from Quotable API |

---

## How It Works

1. Smile greets you based on the time of day
2. You speak a command or question into your microphone
3. Your speech is converted to text via Google's Speech API
4. The text is sent to Gemini AI which generates a response
5. The response is spoken back to you via `pyttsx3`

---

## File Structure

```
Smile/
├── finalproject.py     # Main application
├── requirements.txt    # Project dependencies
└── README.md
```

### Key Functions in `finalproject.py`

| Function | What it does |
|----------|-------------|
| `greeting()` | Greets the user based on time of day |
| `listen()` | Captures voice input via microphone |
| `speak()` | Converts text to speech |
| `mrsmyle()` | Starts an AI conversation session with Gemini |
| `getquote()` | Fetches and reads a random motivational quote |
| `printer()` | Formats terminal text output |

---

## Testing

Tests are written with `pytest` and use `unittest.mock` to simulate hardware (microphone) and external APIs without needing a real connection.

```bash
pytest test_project.py
```

| Test | What it covers |
|------|---------------|
| `test_greeting_morning/afternoon/evening` | Correct greeting based on time of day |
| `test_speak` | `pyttsx3` engine is called with the right text |
| `test_time` | `_time()` returns the correct datetime |
| `test_listen` | Speech recognizer returns transcribed text |
| `test_getquote` | Quote API response is parsed and formatted correctly |
| `test_replace_math_expressions` | Math symbols (², ³) are converted to spoken words |
| `test_mrsmyle` | Gemini AI receives the user's message correctly |
| `test_main` | Main loop calls `listen()` and handles exit command |

All external dependencies (microphone, Google Speech API, Gemini AI, Quotable API) are mocked so tests run fully offline.

---

## Design Decisions

**Why Gemini 1.5 Flash?**
After testing multiple models, Gemini 1.5 Flash offered the best balance of speed and response quality — fast enough for real-time voice interaction without sacrificing accuracy.

**Why pyttsx3?**
It works offline, supports multiple platforms, and allows full control over voice, speed, and language — no extra audio dependencies needed.

**Math expressions?**
A custom parser converts symbols like superscripts and fractions into speakable text, so Smile can handle technical queries out loud.

---

## Author

Built by **[Simbarashe Kamwara]**
🔗 [LinkedIn](https://linkedin.com/in/simbarashekamwara) · [GitHub](https://github.com/simbarashekamwara)

---

> CS50P Final Project — 2026
