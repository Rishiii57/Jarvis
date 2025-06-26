# 🤖 Jarvis Voice Assistant (Python)

Jarvis is a Python-based voice assistant that listens to voice commands, performs web-based tasks, and speaks responses. It can:
- Open popular websites
- Play specific songs (via a custom music library)
- Fetch weather updates
- Read out the latest news headlines

---

## 🚀 Features

- 🎤 **Voice Recognition** using `speech_recognition`
- 🗣 **Text-to-Speech** using `pyttsx3`
- 🌐 **Web Integration** to open sites like Google, YouTube, Netflix, etc.
- 📰 **News API** to fetch top headlines
- 🌦️ **OpenWeatherMap API** for current weather reports
- 🎶 **Custom Music Library** support
- 🔐 Uses `.env` for storing API keys and location

---

## 📁 Project Structure

```bash
.
├── jarvis.py              # Main assistant code
├── .env                   # Environment variables (API keys and coordinates)
├── musiclib.py            # Dictionary mapping songs to URLs
├── README.md              # You're reading it now
