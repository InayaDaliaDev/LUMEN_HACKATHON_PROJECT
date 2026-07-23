🧠 LUMEN

STATUS: ACTIVE · BUILT FOR: PROMETHEUS JULY AI HACKATHON · BY A STUDENT, FOR STUDENTS

Understand how your brain actually works — then talk to it.

🚨 THE PROBLEM

Most students get the same advice: "study more," "focus better," "just be disciplined." That advice ignores a simple fact: not everyone's brain runs the same way.

Some people learn best by talking out loud. Others need silence and isolation. Some panic-sprint before a deadline and somehow pull it off. Others freeze the moment a prompt is too open-ended. None of that is a flaw — it's just a different operating system, and most students never get to see their own.

LUMEN exists to close that gap.

🚀 THE SOLUTION

LUMEN is a 3-step self-understanding tool:

[1] QUIZ        →  24 scenario-based questions about how you actually work, study, and react under pressure
[2] PROFILE      →  A personalized breakdown: your patterns, your blind spots, one concrete tip per pattern
[3] CHATBOT      →  Ask follow-up questions — answered *in the context of your specific profile*, not generic advice
✨ Bonus feature: "What If"

A one-click prompt that asks the chatbot: "Given my profile, what should I expect — and how do I adapt — going into middle school / high school / college?" Instead of a separate static database, it reuses the same profile-aware chatbot engine, so the advice stays personalized instead of generic.

🛠 TECH STACK
diff
+ [ENGINE]    Python 3.x 
+ [UI]        Streamlit — multi-page app, session-state driven
+ [AI]     LLM prompt engineering (Gemini) — chatbot responses are conditioned on the user's quiz vectors + labels
+ [DATA]      Self-contained question bank (data/question.py) — 24 questions × 4 options, each mapped to a label,
              an actionable tip, and a 4-axis weight vector

▶️ RUN IT LOCALLY
bash
git clone <your-repo-url>
cd lumen
pip install -r requirements.txt
streamlit run app.py
📂 PROJECT STRUCTURE
lumen/
├── app.py                 # Entry point / onboarding
├── pages/
│   ├── Quiz.py             # The 24-question flow
│   ├── Advices.py          # Personalized profile report
│   └── Chatbot.py          # Profile-aware chat + "What If" prompts
├── data/
│   └── question.py         # Question bank (id, section, question, options, labels, advice, vectors)
└── requirements.txt
⚠️ HONEST LIMITATIONS

LUMEN is a self-reflection tool inspired by concepts in cognitive and educational psychology — it is not a clinically validated psychometric instrument. The four axes it scores (information bandwidth, execution rigor, chaos tolerance, cognitive endurance) are internal weights we designed for this app, not an established, peer-reviewed scale. Treat your profile as a mirror to start a conversation with yourself, not a diagnosis.

🔒 PRIVACY BY DESIGN

Your answers and profile live only in st.session_state for the duration of your session. Nothing is written to a database, nothing persists after you close the tab. What you learn about yourself stays with you.

🗺 ROADMAP
 Export profile as a shareable PDF/image
 "What If" presets for more life transitions (first job, team project, remote work)
 Multi-language support
 Optional teacher/mentor view (aggregate, anonymized patterns for a classroom)
👤 TEAM

Built solo by a 15-year-old developer for the Prometheus July AI Hackathon.