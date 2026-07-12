# 🌱 AI Agriculture Assistant

An AI-powered agriculture assistant that helps users identify plants, detect diseases, analyze symptoms, provide treatment recommendations, and monitor plant health over time.

---

# Features

## 🌿 Plant Identification

- Identify plant species from uploaded images
- Scientific name
- Plant family
- Confidence score
- Healthy or Diseased status

---

## 🦠 Disease Detection

- Detect diseases using Computer Vision
- Confidence score
- Severity level
- Disease description
- Symptoms
- Cause

---

## 💊 Treatment Recommendation

- Organic treatment
- Chemical treatment
- Home remedies
- Prevention tips
- Recovery estimate

---

## 🤖 AI Agriculture Chatbot

Powered by OpenRouter.

Supports

- English
- Hindi
- Hinglish

Users can ask questions such as

- What disease is this?
- How often should I water this plant?
- Is neem oil useful?
- Which fertilizer should I use?
- Can this disease spread?

---

## 🌦 Weather Analysis

Uses weather data to estimate disease risk.

Shows

- Temperature
- Humidity
- Rain
- Wind Speed

AI also predicts

- Fungal Disease Risk
- Heat Stress
- Water Stress

---

## 🎤 Voice Assistant

Speech-to-Text

- AssemblyAI

Text-to-Speech

- Piper TTS

Supports

- Hindi
- English

---

## 📈 Progress Tracking

Compare old and new plant images.

Shows

- Improved
- Same
- Worse

Generates recovery reports.

---

## 🗂 Scan History

Stores

- Uploaded Image
- Plant Name
- Disease
- Treatment
- Weather
- Date

---

# Technology Stack

## Frontend

- React
- Vite
- TypeScript
- Tailwind CSS
- Axios

---

## Backend

- Python
- FastAPI
- SQLAlchemy
- OpenCV
- Pydantic

---

## AI

- PlantNet API
- YOLOv11
- OpenRouter
- OpenCV

---

## Voice

- AssemblyAI
- Piper TTS

---

## Weather

- OpenWeatherMap API

---

## Database

Development

- SQLite

Production

- PostgreSQL

---

# Project Structure

```
AI-Agriculture-Assistant/

├── frontend/
├── backend/
├── datasets/
├── trained_models/
├── docs/
├── .env
├── .gitignore
└── README.md
```

---

# Workflow

```
User Uploads Image
        │
        ▼
PlantNet API
        │
        ▼
Plant Identified
        │
        ▼
YOLOv11 Disease Detection
        │
        ▼
OpenRouter AI Explanation
        │
        ▼
Weather Analysis
        │
        ▼
Treatment Recommendation
        │
        ▼
Save History
        │
        ▼
Display Result
```

---

# APIs Used

| Service | Purpose |
|----------|---------|
| PlantNet API | Plant Identification |
| OpenRouter | AI Chatbot & Diagnosis |
| OpenWeatherMap | Weather Information |
| AssemblyAI | Speech-to-Text |
| Piper | Text-to-Speech |

---

# Future Improvements

- Pest Detection
- Soil Analysis
- Fertilizer Recommendation
- Irrigation Recommendation
- Mobile App
- Drone Support
- Satellite Image Support
- IoT Sensor Integration

---

# License

MIT License

---

# Author

Rahul Yadav

B.Tech CSE

AI Agriculture Assistant Project