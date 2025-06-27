# 🤖 Jarvis Voice Assistant (Python)

Jarvis is a Python-based voice assistant that listens to your voice, performs intelligent tasks using online services, and responds with speech. It can:
- Open websites
- Play songs (via YouTube API)
- Fetch weather updates
- Read out the latest news headlines
- Answer questions using AI (via OpenRouter API)

---

## 🚀 Features

- 🎤 **Voice Recognition** using `speech_recognition`
- 🗣 **Text-to-Speech** using `pyttsx3`
- 🌐 **Web Integration** to open sites like Google, YouTube, Netflix, etc.
- 🎶 **Music Support** using direct links and YouTube search
- 📰 **News API** integration (via NewsAPI.org)
- 🌦️ **Weather API** integration (via OpenWeatherMap)
- 🤖 **AI Assistant** using OpenRouter API (supports models like DeepSeek)
- 🔐 Secure API key management using `.env`

---

## 🧠 AI Integration

Jarvis uses the [OpenRouter](https://openrouter.ai) platform to generate intelligent responses for general questions using large language models like `deepseek/deepseek-r1:free`. This allows the assistant to respond smartly to open-ended queries like:

- “What is the capital of France?”
- “Tell me a joke.”
- “Summarize Newton’s laws.”

---

## 📁 Project Structure

```bash
.
├── jarvis.py              # Main assistant code
├── musiclib.py            # Song title to YouTube URL mappings
├── .env                   # API keys and location data

