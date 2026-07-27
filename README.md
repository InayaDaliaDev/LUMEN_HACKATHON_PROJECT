# 🧠 LUMEN — The Metacognitive Mirror

> **Prometheus July AI Challenge 2026** · *Built by a student, for students*

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.36+-red)
![LangGraph](https://img.shields.io/badge/langgraph-1.2+-purple)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🚨 The Problem

Most educational tools treat every brain as identical.

- Students are told to *"study harder"* — but nobody tells them *how* their specific brain actually works.
- Some people freeze under open-ended prompts; others thrive on panic-sprints.
- Some need absolute silence; others need background chatter to focus.
- Generic advice fails **80%** of students — not because they're lazy, but because they're running a different **operating system** and never get to see their own source code.

**LUMEN exists to change that.**

---

## 🚀 The Solution

LUMEN is a **3-step self-understanding engine** that maps your cognitive fingerprint and gives you *actionable, non-generic* strategies — not empty platitudes.

| Step | Module | What it does |
| :--- | :--- | :--- |
| **1** | **Neural Assessment** | 24 scenario-based questions that probe how you *actually* react under academic pressure, distraction, and ambiguity. |
| **2** | **Builder Blueprint** | Instantly generated profile: your **dominant archetype**, **4-axis vector scores** (Information Bandwidth, Execution Rigor, Chaos Tolerance, Cognitive Endurance), and **one personalized technique per blind spot**. |
| **3** | **SYNAPSE Mentor** | A LangGraph-powered AI mentor that answers your follow-up questions **strictly using a verified technique library** — never generic "make a flashcard" advice. |
| **Bonus** | **CHRONOS Simulation** | A predictive "What If" engine that simulates your academic trajectory in specific environments (e.g., *"What happens if I take this profile into a competitive European university?"*) — powered by a deterministic LangGraph phase-router (Opening → Challenge → Resolution). |

---

## ✨ Why This Is Different (Not Just Another Chatbot)

1. **Metacognition First** — We don't just answer questions; we make you understand *why* you think the way you do.
2. **Grounded AI** — The mentor cannot invent study techniques. It must pick from a **hard-coded library** of evidence-based frameworks (Feynman Technique, Spaced Repetition, Interleaving, Desirable Difficulties, etc.) based on your specific weakest axis. No hallucinations.
3. **LangGraph State Machines** — Instead of a single chaotic prompt, CHRONOS uses deterministic phase-routing (`Opening → Challenge → Resolution`) to pace the simulation like a real narrative.
4. **Privacy by Design** — Everything lives in `st.session_state`. No database. No tracking. Close the tab, and your data vanishes.

---

## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend / UI** | Streamlit (multi-page app, session-state driven) |
| **Orchestration** | LangGraph + LangChain |
| **LLM** | Google Gemini 2.5 Flash / Pro (via `langchain-google-genai`) |
| **State Management** | `MemorySaver` checkpointer (per-thread isolation) |
| **Data** | Self-contained `data/question.py` — 24 questions × 4 options, each with labels, vectors, and actionable advice |

---

## 📦 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/your-username/lumen.git
cd lumen
2. Create a virtual environment (recommended)
bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
3. Install dependencies
bash
pip install -r requirements.txt
4. Set up your Gemini API key
LUMEN uses Google's Gemini API for the mentor and simulation engines.

Option A (Recommended for testing):
Create a .streamlit/secrets.toml file:

toml
GEMINI_API_KEY = "your-actual-api-key-here"
Option B:
Paste your key directly into the sidebar of the running app (it persists for the session).

Get your free Gemini API key: Google AI Studio

5. Run the app
bash
streamlit run lumen_app.py
⚠️ Note: The entry point is lumen_app.py, not app.py.

📂 Project Structure
text
lumen/
├── lumen_app.py               # Entry point + navigation + profile setup
├── requirements.txt
├── README.md
│
├── data/
│   └── question.py            # 24-question database (sections, options, vectors, advice)
│
├── pages/
│   ├── 01_Assessment.py       # Quiz flow with progress bar + defensive parsing
│   ├── Advices.py             # The "Builder Blueprint" report (normalized scores)
│   ├── Chatbot.py             # LangGraph-based SYNAPSE mentor
│   ├── What_If.py             # CHRONOS predictive simulation (LangGraph phase-router)
│   └── TheOldDays.py          # Historical immersion (bonus narrative engine)
│
└── .streamlit/
    └── secrets.toml           # (optional) Store your Gemini key here
🧪 How It Works (Deep Dive)
Assessment Engine (01_Assessment.py)
Questions are loaded from data/question.py.

Each option maps to a 4-vector weight and a specific advice string.

After completion, core_vectors are cached in st.session_state.

Blueprint Generator (Advices.py)
Computes theoretical min/max for each axis across all questions (not an arbitrary scale).

Normalizes your raw score to a 0–100% range.

Dynamically generates a non-generic strategic blueprint from your strongest and weakest axes, rather than a static lookup table.

SYNAPSE Mentor (Chatbot.py)
Injects your dominant archetype, strongest axis, and weakest axis into the system prompt.

Uses a hardcoded TECHNIQUE_LIBRARY (Feynman, Spaced Repetition, Dual Coding, etc.).

A deterministic select_priority_techniques() node picks the most relevant techniques for your profile before the LLM generates a response — ensuring the AI never invents fake methods.

CHRONOS Simulation (What_If.py)
Uses a LangGraph state machine with three specialized nodes:

opening — Sets the institutional scene (e.g., "Elite University in Europe").

challenge — Introduces a concrete friction point based on your weak axis.

resolution — Offers a tactical remediation blueprint.

The phase-router counts turns and advances the narrative deterministically — no prompt-juggling, no repetitive openings.

🔒 Privacy & Ethics
Zero data persistence — All answers, profiles, and chat histories live in st.session_state and are destroyed when you close the browser tab.

No tracking, no analytics, no third-party cookies.

Honest disclaimer: LUMEN is a self-reflection tool inspired by educational psychology — not a clinically validated psychometric instrument. Use it as a mirror, not a diagnosis.

🗺 Roadmap (Post-Hackathon)
□ Export profile as a shareable PDF / image
□ "What If" presets for more life transitions (first job, team project, remote work)
□ Multi-language support (French, Spanish, Arabic)
□ Optional teacher/mentor view (aggregated, anonymized classroom patterns)

Note : I know a professional in Psycologie, i might try to get their validation and ask them to be my mentor to make this project rigorous. She said she is already interested.

👤 Team
Built solo by a 15-year-old developer for the Prometheus July AI Hackathon.

"I built LUMEN because I was tired of hearing 'just focus' from people who didn't know how my brain worked. Now I can show them."

📄 License
MIT — Use it, fork it, learn from it. Just give credit where it's due.

🙏 Acknowledgments
Prometheus for hosting the challenge

Google Gemini for the LLM backbone

LangChain / LangGraph for the orchestration framework

Streamlit for making Python UI accessible

