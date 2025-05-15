
# 📚 Personalized Learning Roadmap Generator 🧠
*An AI-powered tool to generate structured learning paths using LLMs and curated online resources.*

![Project Banner](https://img.shields.io/badge/AI-Learning%20Assistant-blue?style=for-the-badge)

> Built with FastAPI · Streamlit · GitHub-hosted LLMs

---

## 📌 Overview

Learning a new topic can be overwhelming due to the scattered and unstructured nature of online content.  
This project solves that by using a Large Language Model (LLM) to generate a **personalized, milestone-based learning roadmap** with curated resources.

Users input a topic (e.g., “Data Science” or “ReactJS”), and the system responds with:

✅ Prerequisites  
✅ Estimated learning time  
✅ Step-by-step milestones  
✅ Recommended courses, articles, and videos

---

## 🛠️ Tech Stack

| Layer        | Technology             |
|--------------|------------------------|
| Frontend     | Streamlit              |
| Backend      | FastAPI (Python)       |
| LLM          | GitHub-hosted GPT Model (`https://models.github.ai`) |
| Parsing/Validation | Pydantic, Regex     |
| API Clients  | `openai` Python SDK (customized for GitHub proxy) |
| Deployment   | Localhost (dev)        |

---

## 🎯 Features

- 🧠 Uses LLMs to generate topic-specific roadmaps
- 🔗 Fetches 2–3 curated resources per milestone
- 📋 Streamlit-based UI for input/output display
- 🧪 FastAPI backend with robust validation
- 🧵 Modular and easy to extend with APIs or user history

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/your-username/personalized-learning-roadmap.git
cd personalized-learning-roadmap
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up your `.env` file
Create a `.env` file in the root folder:

```env
GITHUB_TOKEN=your_github_api_key_here
OPENAI_MODEL=gpt-4o
```

### 4. Run the backend (FastAPI)
```bash
uvicorn main:app --reload
```

### 5. Run the frontend (Streamlit)
```bash
streamlit run streamlit_app.py
```

---

## 📦 Folder Structure

```
├── main.py                # FastAPI app
├── streamlit_app.py       # Streamlit frontend
├── roadmap_generator.py   # LLM prompt + response parsing
├── models.py              # Pydantic models
├── utils.py               # JSON extractor
├── config.py              # API key config
├── requirements.txt
└── .env
```

---

## 🔮 Future Scope

- ✅ Add user account system (track progress)
- ✅ Export roadmap to Notion/Google Docs
- ✅ Quiz or checkpoint generator per milestone
- ✅ Deploy using Render or Streamlit Cloud
- ✅ Feedback loop for roadmap quality rating

---

## 🤝 Contributing

Pull requests and suggestions are welcome!  
If you find an issue or want to add a feature, feel free to fork and submit a PR.

---

## 📜 License

MIT License © 2024 [Mohd Khalid Altaf Ahmed Shaikh](https://github.com/Ks-Aech)

---
