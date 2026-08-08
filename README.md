# 🧠 LUMEN

**🔗 Live app:** https://lumenhackathonproject-zl2krm44mqm5we6d2arztr.streamlit.app/

> *Built by a student, for students*

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Python](https://img.shields.io/badge/python-3.9+-blue)
![Streamlit](https://img.shields.io/badge/streamlit-1.36+-red)
![LangGraph](https://img.shields.io/badge/langgraph-1.2+-purple)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 🚨 The Problem

Most educational tools treat every brain as identical.

- Students are told to *"just focus"* — but nobody tells them *how* their specific brain actually works.
- Some people freeze under open-ended prompts; others thrive on panic-sprints.
- Some need absolute silence; others need background chatter to focus.
- Generic advice fails most students — not because they're lazy, but because they're running a different **operating system** and never get to see their own source code.

**LUMEN exists to change that.**

---

## 🚀 The Solution

LUMEN is a **cognitive self-understanding engine**: it maps how you actually think, then hands you tools that are grounded in your specific profile — not generic platitudes.

| Step | Module | What it does |
| :--- | :--- | :--- |
| **1** | **Neural Assessment** | 24 scenario-based questions that probe how you *actually* react under academic pressure, distraction, and ambiguity. |
| **2** | **Strategic Countermeasures** | Instantly generated profile: your **dominant archetype**, **4-axis vector scores** (Information Bandwidth, Execution Rigor, Chaos Tolerance, Cognitive Endurance), and personalized advice per blind spot. |
| **3** | **Mr. Brown — AI Mentor** | A LangGraph-powered mentor that answers your follow-up questions **strictly using a verified technique library**, tuned for rigorous, no-fluff academic and technical guidance. |
| **4** | **CHRONOS Simulation ("What If")** | A predictive engine that simulates your academic trajectory in specific environments (e.g., *"what happens if I take this profile into a competitive European university?"*) — powered by a deterministic LangGraph phase-router. |
| **5** | **Temporal Logs ("The Old Days")** | A "multiverse" narrative simulation exploring alternate academic/institutional timelines based on your parameters. |
| **6** | **Quiz Generator** | Drop in any text or notes — Gemini turns it into a graded multiple-choice quiz on the spot. |
| **7** | **Neural Roadmap** | A personalized 12-day action plan generated from your actual cognitive vectors from Step 1. |

---

## ✨ Why This Is Different (Not Just Another Chatbot)

1. **Metacognition First** — We don't just answer questions; we make you understand *why* you think the way you do.
2. **Grounded AI** — Mr. Brown cannot invent study techniques. It must pick from a **hard-coded library** of evidence-based frameworks (Feynman Technique, Spaced Repetition, Interleaving, Desirable Difficulties, etc.) based on your specific weakest axis. No hallucinated methods.
3. **LangGraph State Machines** — Instead of a single chaotic prompt, CHRONOS uses deterministic phase-routing to pace each simulation like a real narrative, and every AI module runs on a checkpointed LangGraph graph rather than raw prompt-stuffing.
4. **Privacy by Design** — Everything currently lives in `st.session_state`. No database is wired in yet. Close the tab, and your data vanishes. *(see Roadmap — optional persistence is being explored, not live.)*

---

## 🛠 Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Frontend / UI** | Streamlit (multi-page app via `st.navigation`, session-state driven) |
| **Orchestration** | LangGraph + LangChain |
| **LLM** | Google Gemini (`gemini-2.5-flash` default, with `gemini-2.5-flash-lite` and `gemini-3.5-flash` as selectable/fallback options) via `langchain-google-genai` |
| **State Management** | `MemorySaver` checkpointer (per-thread isolation) + a centralized `core/centralstate.py` session-state manager |
| **Data** | Self-contained `data/question.py` — 24 questions × 4 options, each with labels, vectors, and actionable advice |

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/lumen.git
cd lumen
```

### 2. Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your Gemini API key
LUMEN uses Google's Gemini API for the mentor, quiz, roadmap, and simulation engines.

**Option A (recommended for local testing):** create `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your-actual-api-key-here"
```

**Option B:** paste your key directly into the sidebar of the running app (it persists for the session only).

Get a free Gemini API key at [Google AI Studio](https://aistudio.google.com/).

### 5. Run the app
```bash
streamlit run lumen_app.py
```
⚠️ The entry point is `lumen_app.py`, not `app.py`.

---

## 📂 Project Structure
```
LUMEN_HACKATHON_PROJECT/
├── lumen_app.py               # Entry point + navigation + profile setup
├── requirements.txt
├── README.md
│
├── core/
│   ├── centralstate.py        # Single source of truth for st.session_state
│   ├── disclaimer.py          # Non-professional / no-liability disclaimer, shown on entry
│   ├── scoring.py             # Cognitive vector scoring helpers
│   └── utils.py                # Shared helpers: text extraction, key validation, JSON parsing
│
├── data/
│   └── question.py            # 24-question database (sections, options, vectors, advice)
│
└── pages/
    ├── 01_Assessment.py        # Quiz flow with progress bar + defensive parsing
    ├── 02_Advices.py           # The "Strategic Countermeasures" report (normalized scores)
    ├── 03_Mr.Brown.py          # LangGraph-based AI mentor
    ├── 04_What_If.py           # CHRONOS predictive simulation (LangGraph phase-router)
    ├── 05_TheOldDays.py        # Multiverse / alternate-timeline narrative engine
    ├── 06_Quiz_Generator.py    # Text/notes → graded multiple-choice quiz
    └── 07_Planning_Generator.py # 12-day roadmap generated from your cognitive vectors
```

---

## 🧪 How It Works (Deep Dive)

### Assessment Engine (`01_Assessment.py`)
- Questions are loaded from `data/question.py`.
- Each option maps to a 4-vector weight and a specific advice string.
- After completion, `core_vectors` are cached in `st.session_state` for every downstream page to reuse.

### Blueprint Generator (`02_Advices.py`)
- Computes theoretical min/max for each axis across all questions (not an arbitrary scale).
- Normalizes your raw score to a 0–100% range.
- Dynamically generates a non-generic strategic blueprint from your strongest and weakest axes, rather than a static lookup table.

### Mr. Brown — AI Mentor (`03_Mr.Brown.py`)
- Injects your dominant archetype, strongest axis, and weakest axis into the system prompt.
- Uses a hardcoded `TECHNIQUE_LIBRARY` (Feynman, Spaced Repetition, Dual Coding, etc.).
- A deterministic `select_priority_techniques()` node picks the most relevant techniques for your profile *before* the LLM generates a response — the AI never invents fake methods.
- Persona: a sharp, rigor-first mentor with zero patience for fluff — built for a self-directed, math/code-oriented user rather than a soft "life coach" tone.

### CHRONOS Simulation (`04_What_If.py`)
- Uses a LangGraph state machine with specialized phases (Opening → Challenge → Resolution).
- Introduces a concrete friction point based on your weak axis, then a tactical remediation blueprint.
- The phase-router advances the narrative deterministically — no prompt-juggling, no repetitive openings.

### Quiz Generator (`06_Quiz_Generator.py`)
- Paste or upload any text/notes.
- Gemini returns a structured JSON quiz, rendered as an interactive graded multiple-choice test with a final score.

### Neural Roadmap (`07_Planning_Generator.py`)
- Locked until the Assessment is completed.
- Feeds your real `core_vectors` into Gemini to generate a 12-day personalized action plan, rendered day by day.

---

## 🔒 Privacy & Ethics
- **No live persistence** — all answers, profiles, and chat histories currently live in `st.session_state` and are destroyed when you close the browser tab. A Supabase project has been provisioned for a possible future opt-in "save my profile" feature, but **it isn't connected to the app yet** — nothing you enter is written to it today.
- No tracking, no analytics, no third-party cookies.
- **Honest disclaimer, shown on entry:** LUMEN is a self-reflection tool inspired by educational psychology — not a clinically validated psychometric instrument, and nobody behind it is a licensed psychologist, therapist, or doctor. Use it as a mirror, not a diagnosis. If something ever touches on your mental health or wellbeing, talk to a real, qualified person.

---

## 🗺 Roadmap (Post-Hackathon)
- [ ] Optional Supabase-backed persistence (save your profile across devices/sessions — opt-in only, nothing forced)
- [ ] Export profile as a shareable PDF / image
- [ ] "What If" presets for more life transitions (first job, team project, remote work)
- [ ] Multi-language support (French, Spanish, Arabic)
- [ ] Optional teacher/mentor view (aggregated, anonymized classroom patterns)

*Note: I know a professional in psychology who has expressed interest in reviewing the project and potentially mentoring it, to help make the underlying framework more rigorous.*

---

## 👤 Team
Built solo by a 15-year-old developer, originally for the Prometheus July AI Challenge and extended further for **ReverieHacks 2026**.

> "I built LUMEN because I was tired of hearing 'just focus' from people who didn't know how my brain worked. Now I can show them."

---

## 📄 License
MIT — Use it, fork it, learn from it. Just give credit where it's due.

## 🙏 Acknowledgments
- Prometheus and ReverieHacks for hosting the challenges
- Google Gemini for the LLM backbone
- LangChain / LangGraph for the orchestration framework
- Streamlit for making Python UI accessible