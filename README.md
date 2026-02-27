<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,30,35&height=170&section=header&text=YouTube%20Viral%20Predictor&fontSize=46&fontAlignY=35&animation=twinkling&fontColor=ffffff&desc=Fine-Tuned%20Llama%202%207B%20%7C%20Predict%20Video%20Virality%20Before%20Publishing&descAlignY=55&descSize=18" width="100%" />

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](.)
[![Llama 2](https://img.shields.io/badge/Llama_2-7B-0467DF?style=for-the-badge&logo=meta&logoColor=white)](.)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](.)
[![Railway](https://img.shields.io/badge/Railway-Deployed-0B0D0E?style=for-the-badge&logo=railway&logoColor=white)](.)

**Predict whether a YouTube video will go viral based on its title, description, and metadata.**

</div>

---

## Why This Exists

Creators spend hours crafting content but have no way to test if their title, description, or topic will resonate before hitting publish. This tool uses a fine-tuned Llama 2 7B model to predict virality based on patterns learned from real YouTube data.

Input your video metadata. Get a virality score and actionable suggestions.

---

## Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                YouTube Viral Predictor                        │
│                                                               │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐  │
│   │   Web UI      │───→│  Flask API   │───→│  Llama 2 7B  │  │
│   │  (HTML/CSS)   │    │  (app.py)    │    │  Fine-tuned  │  │
│   │  Input form   │    │  Endpoint    │    │  Inference    │  │
│   └──────────────┘    └──────────────┘    └──────┬───────┘  │
│                                                    │          │
│                              ┌─────────────────────▼────┐    │
│                              │  Prediction Response     │    │
│                              │  ├─ Virality score       │    │
│                              │  ├─ Category analysis    │    │
│                              │  └─ Suggestions          │    │
│                              └──────────────────────────┘    │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

---

## How It Works

| Step | What Happens | Technology |
|------|-------------|------------|
| **1** | Enter video title, description, tags, and category | HTML form |
| **2** | Metadata sent to Flask API endpoint | Flask server |
| **3** | Input tokenized and processed for inference | Transformers |
| **4** | Fine-tuned Llama 2 7B generates prediction | LoRA/QLoRA weights |
| **5** | Virality score + analysis returned to UI | JSON response |
| **6** | Results displayed with actionable insights | Frontend render |

---

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| **Llama 2 7B over GPT API** | Self-hosted = $0/request, no rate limits |
| **Fine-tuning over prompt engineering** | Domain-specific patterns learned from real data |
| **Flask over FastAPI** | Lightweight, sufficient for single-model serving |
| **Railway deployment** | Simple Python deployment with Procfile |

---

## Quick Start

```bash
git clone https://github.com/ajay-automates/youtube-viral-predictor.git
cd youtube-viral-predictor
pip install -r requirements.txt
python app.py
# Open http://localhost:7860
```

### Deploy on Railway

1. Connect this repo to Railway
2. Railway auto-detects Python via Procfile
3. Model loads on first request

---

## Project Structure

```
youtube-viral-predictor/
├── app.py               # Flask server + model inference
├── index.html           # Standalone web UI
├── templates/           # Jinja2 templates
├── requirements.txt     # Python dependencies
└── Procfile             # Railway deployment config
```

---

## Tech Stack

`Python` `Llama 2 7B` `LoRA/QLoRA` `Flask` `Transformers` `Railway` `HTML/CSS`

---

## Related Projects

| Project | Description |
|---------|-------------|
| [Advanced Resume Analyzer](https://github.com/ajay-automates/advanced-resume-analyzer-qlora) | Fine-tuned Gemma 3 4B with QLoRA |
| [AI Code Review Bot](https://github.com/ajay-automates/ai-code-review-bot) | LLMOps with Claude for automated PR reviews |
| [AJ Content Calendar](https://github.com/ajay-automates/aj-content-calendar) | Auto-updated daily AI news dashboard |

---

<div align="center">

**Built by [Ajay Kumar Reddy Nelavetla](https://github.com/ajay-automates)** · February 2026

*Know if your video will pop — before you publish.*

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=24,30,35&height=100&section=footer" width="100%" />

</div>
