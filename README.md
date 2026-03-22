# 🔍 AI Code Reviewer

An AI-powered code review tool built with **Python**, **Flask**, and the **Anthropic Claude API**. Paste any code snippet and get instant structured feedback on bugs, quality, performance, security, and improvements.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.1-black?style=flat-square&logo=flask)
![Claude](https://img.shields.io/badge/Claude-Sonnet-orange?style=flat-square)

---

## ✨ Features

- 🐛 **Bug Detection** — Catches logic errors and potential runtime issues
- 📐 **Code Quality** — Reviews naming, structure, readability, and style
- ⚡ **Performance** — Flags inefficiencies and suggests improvements
- 🔒 **Security** — Detects vulnerabilities like SQL injection or hardcoded secrets
- 🌐 **Multi-language** — Supports Python, Java, JavaScript, TypeScript, Go, Rust, SQL, Bash, C++
- 🎯 **Scored Review** — Each review ends with a 1–10 score and explanation

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-code-reviewer.git
cd ai-code-reviewer
```

### 2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
cp .env.example .env
# Open .env and add your Anthropic API key
```

Get your free API key at: https://console.anthropic.com

### 5. Run the app
```bash
python app.py
```

Open your browser at `http://localhost:5000`

---

## 🗂️ Project Structure

```
ai-code-reviewer/
├── app.py               # Flask backend + Claude API integration
├── templates/
│   └── index.html       # Frontend UI
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variable template
├── .gitignore
└── README.md
```

---

## 🧠 How It Works

1. User pastes code and selects a language (or uses auto-detect)
2. The Flask backend sends the code to Claude via the Anthropic API
3. Claude returns structured feedback: bugs, quality, performance, security, and a score
4. The frontend renders the review in real time

---

## 🛠️ Tech Stack

| Layer    | Technology         |
|----------|--------------------|
| Backend  | Python, Flask      |
| AI Model | Anthropic Claude Sonnet |
| Frontend | HTML, CSS, Vanilla JS |
| Config   | python-dotenv      |

---

## 📦 Deployment

You can deploy this for free on **Render**:

1. Push your repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service
3. Connect your GitHub repo
4. Set `ANTHROPIC_API_KEY` as an environment variable in Render's dashboard
5. Set build command: `pip install -r requirements.txt`
6. Set start command: `gunicorn app:app`

---

## 📄 License

MIT License — feel free to use and modify.
