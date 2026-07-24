import streamlit as st
from collections import Counter
from data.question import ALL_QUESTIONS

# ==============================================================================
# 1. SESSION INTEGRITY CHECK
# ==============================================================================
if 'answers' not in st.session_state or not st.session_state.answers:
    st.error("🛑 No answers detected in session memory.")
    st.markdown("You need to complete the assessment before unlocking this report.")
    if st.button("🚀 Return to Assessment", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

if 'user_profile' not in st.session_state:
    st.session_state.user_profile = {"pseudo": "Anonymous Builder", "gender": "Unmapped", "initialized": True}

user_profile = st.session_state.user_profile
pseudo = (user_profile.get("pseudo", "Anonymous Builder") or "").strip() or "Operator"
classification = user_profile.get("gender", "Unmapped Human")
answers = st.session_state.answers


# ==============================================================================
# 2. DATA PARSING ENGINE
# ==============================================================================
sections_data = {}
all_labels = []
vector_totals = {
    "information_bandwidth": 0.0,
    "execution_rigor": 0.0,
    "chaos_tolerance": 0.0,
    "cognitive_endurance": 0.0,
}

if not ALL_QUESTIONS:
    st.error("⚠️ CRITICAL: The global ALL_QUESTIONS database is empty or missing.")
    st.stop()

for q in ALL_QUESTIONS:
    q_id = q.get('id')
    if q_id and q_id in answers:
        user_choice_key = answers.get(q_id)
        options = q.get("options", {})
        if user_choice_key in options:
            option_data = options[user_choice_key]
            sec_name = q.get('section', 'General Mindset')

            if sec_name not in sections_data:
                sections_data[sec_name] = []

            sections_data[sec_name].append({
                "q_id": str(q_id),
                "question": q.get('question', 'Missing Question'),
                "choice_text": option_data.get('text', 'No selection'),
                "label": option_data.get('label', 'Standard Processing'),
                "advice": option_data.get('advice', 'No direct advice available.')
            })

            all_labels.append(option_data.get('label', 'Standard Processing'))

            for v_key, v_val in (option_data.get("vectors", {}) or {}).items():
                if v_key in vector_totals:
                    try:
                        vector_totals[v_key] += float(v_val)
                    except (TypeError, ValueError):
                        continue

if not all_labels:
    st.error("⚠️ We couldn't extract any behavioral patterns. The data matrix is empty.")
    if st.button("🔄 Try Assessment Again"):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

label_counts = Counter(all_labels)
dominant_archetype = str(label_counts.most_common(1)[0][0]).strip()


# ==============================================================================
# 3. THEORETICAL RANGE ENGINE
# ==============================================================================
# For each axis, we compute the actual min/max achievable across every
# question in the bank — the best-case and worst-case answer for that axis,
# summed across all 24 questions. This gives a real, defensible 0-100%
# normalization instead of an arbitrary guessed scale, and it's cheap: it
# only reads the static question bank, no extra input needed.
theoretical_min = {axis: 0.0 for axis in vector_totals}
theoretical_max = {axis: 0.0 for axis in vector_totals}

for q in ALL_QUESTIONS:
    opts = (q.get("options", {}) or {}).values()
    for axis in vector_totals:
        axis_values = []
        for opt in opts:
            try:
                axis_values.append(float((opt.get("vectors", {}) or {}).get(axis, 0.0)))
            except (TypeError, ValueError):
                axis_values.append(0.0)
        if axis_values:
            theoretical_min[axis] += min(axis_values)
            theoretical_max[axis] += max(axis_values)


def normalize_axis(axis: str) -> int:
    lo, hi = theoretical_min[axis], theoretical_max[axis]
    if hi <= lo:
        return 50
    pct = (vector_totals[axis] - lo) / (hi - lo) * 100
    return max(0, min(100, round(pct)))


normalized_scores = {axis: normalize_axis(axis) for axis in vector_totals}
strongest_key = max(vector_totals, key=vector_totals.get)
weakest_key = min(vector_totals, key=vector_totals.get)

AXIS_DISPLAY_NAMES = {
    "information_bandwidth": "Information Bandwidth",
    "execution_rigor": "Execution Rigor",
    "chaos_tolerance": "Chaos Tolerance",
    "cognitive_endurance": "Cognitive Endurance",
}


# ==============================================================================
# 4. THE BLUEPRINT GENERATOR
# ==============================================================================
# Instead of a hand-written table keyed by archetype label (which could only
# ever cover a handful of the ~78 labels the question bank can produce), the
# strategic report is GENERATED from the two most defining axes: your
# strongest and your weakest. 4 axes x 3 possible "weakest partners" = 12
# distinct, coherent blueprints — every single user gets a report grounded
# in their own numbers, never a generic fallback message.
AXIS_NARRATIVES = {
    "information_bandwidth": {
        "high": {
            "adj": "wide-scanning, pattern-hungry",
            "overreach": "you'll happily juggle five open threads at once, and sometimes lose the plot on which one actually matters right now",
        },
        "low": {
            "adj": "narrow-focus, detail-first",
            "blind_spot": "you do best with one clearly-defined piece of information at a time — throw six requirements at you simultaneously and details start quietly slipping through the cracks",
            "crisis": "under pressure, you'll re-read the same paragraph three times instead of asking someone to just summarize it for you",
            "synergy": "someone who scans the big picture fast and hands you one clean instruction at a time",
        },
    },
    "execution_rigor": {
        "high": {
            "adj": "structured, checklist-driven",
            "overreach": "you'll spend precious minutes perfecting a function nobody asked you to touch yet",
        },
        "low": {
            "adj": "fast-and-loose, ship-first",
            "blind_spot": "clean code and documentation feel like friction when the clock is running — you'll happily duct-tape a fix and move on without asking why it broke",
            "crisis": "when something breaks under deadline pressure, you patch the symptom, not the cause, and it usually resurfaces an hour later",
            "synergy": "someone who's genuinely energized by cleaning up after a sprint and closing the loose ends you left open",
        },
    },
    "chaos_tolerance": {
        "high": {
            "adj": "unshaken by pivots",
            "overreach": "you'll suggest ripping out the whole architecture mid-hackathon because you found a shinier framework at 2am",
        },
        "low": {
            "adj": "stability-seeking",
            "blind_spot": "a sudden scope change or a teammate improvising on the fly costs you real focus — you need the plan to hold still to do your best work",
            "crisis": "when the environment turns chaotic, you go quiet and disengage rather than push back or adapt out loud",
            "synergy": "someone who can absorb last-minute chaos and translate it into one calm, concrete next step for you",
        },
    },
    "cognitive_endurance": {
        "high": {
            "adj": "built for the long grind",
            "overreach": "you'll stay locked on one hard problem for hours, even past the point where a fresh pair of eyes would solve it faster",
        },
        "low": {
            "adj": "built for short, intense bursts",
            "blind_spot": "your best thinking comes in sharp 20-30 minute windows — push past that and your output quietly degrades while you keep typing anyway",
            "crisis": "in a long crunch, you'll keep working out of stubbornness long after your focus has actually left the building",
            "synergy": "someone who can take the wheel on the long, grinding stretches so you can show up fully for the sharp, high-leverage moments",
        },
    },
}


def build_blueprint(strong_key: str, weak_key: str) -> dict:
    strong = AXIS_NARRATIVES[strong_key]["high"]
    weak = AXIS_NARRATIVES[weak_key]["low"]

    tagline = f"{strong['adj'].capitalize()} — and {weak['adj']}."
    blind_spots = (
        f"{weak['blind_spot'].capitalize()}. "
        f"And because you're also {strong['adj']}, {strong['overreach']}."
    )
    crisis_mode = weak['crisis'].capitalize() + "."
    synergy = f"You need {weak['synergy']} — someone who covers exactly the ground where you run thin."

    return {
        "tagline": tagline,
        "blind_spots": blind_spots,
        "crisis_mode": crisis_mode,
        "synergy": synergy,
    }


strategy_block = build_blueprint(strongest_key, weakest_key)


# ==============================================================================
# 5. HIGH-IMPACT REPORT RENDERING
# ==============================================================================
st.markdown("<p style='color: #6366F1; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; margin-bottom: -10px;'>Diagnostic Unlocked</p>", unsafe_allow_html=True)
st.title("🧬 Your Builder Blueprint")
st.divider()

col1, col2, col3 = st.columns(3)
col1.metric(label="BUILDER ALIAS", value=pseudo.upper())
col2.metric(label="OPERATIONAL PROFILE", value=classification.upper())
col3.metric(label="DOMINANT ARCHETYPE", value=dominant_archetype.upper())

st.write("")
st.write("")

left_layout, right_layout = st.columns([5, 4], gap="large")

with left_layout:
    st.markdown("### 🛠️ Hackathon Survival Guide")
    st.caption("Generated from your two most defining traits — not a generic lookup.")

    st.markdown(f"""
    <div style="background-color: #1E1E2E; border-left: 4px solid #6366F1; padding: 18px; border-radius: 6px; margin-bottom: 20px;">
        <div style="font-weight: 700; color: #F3F4F6; font-size: 16px; margin-bottom: 4px;">STRONGEST: {AXIS_DISPLAY_NAMES[strongest_key].upper()} · WEAKEST: {AXIS_DISPLAY_NAMES[weakest_key].upper()}</div>
        <div style="font-style: italic; color: #9CA3AF; font-size: 14px;">"{strategy_block['tagline']}"</div>
    </div>
    """, unsafe_allow_html=True)

    with st.container(border=True):
        st.markdown("🚨 **YOUR BIGGEST BLIND SPOT**")
        st.markdown(strategy_block["blind_spots"])

    with st.container(border=True):
        st.markdown("🔥 **WHAT HAPPENS IN CRISIS MODE**")
        st.markdown(strategy_block["crisis_mode"])

    with st.container(border=True):
        st.markdown("🤝 **YOUR DREAM TEAMMATE**")
        st.markdown(strategy_block["synergy"])

with right_layout:
    st.markdown("### 📊 Your 4-Axis Signature")
    st.caption("Where you land on each core dimension — this is the raw data the blueprint above is built from.")
    st.write("")

    for axis, display_name in AXIS_DISPLAY_NAMES.items():
        pct = normalized_scores[axis]
        tag = ""
        if axis == strongest_key:
            tag = " · strongest"
        elif axis == weakest_key:
            tag = " · weakest"
        st.markdown(f"**{display_name}{tag}**")
        st.progress(pct / 100, text=f"{pct}%")
        st.write("")

    with st.expander("🔬 Raw signal frequency (advanced)"):
        st.caption("How often each specific trait label showed up across your 24 answers.")
        total_metrics = len(all_labels)
        for label_name, count in label_counts.most_common():
            percentage = int((count / total_metrics) * 100)
            st.markdown(f"**{label_name}** — {count}/{total_metrics} ({percentage}%)")


# ==============================================================================
# 6. TACTICAL ADVICE ARCHIVE (per-question, unchanged content, same logic)
# ==============================================================================
st.write("")
st.divider()
st.markdown("### 🔍 Tactical Advice Archive")
st.caption("Based strictly on your choices, here is the granular breakdown by section.")
st.write("")

if sections_data:
    tab_names = [name.split(":")[1].strip() if ":" in name else name for name in sections_data.keys()]
    valid_tabs = [name for name in tab_names if name]

    if valid_tabs:
        tabs = st.tabs(valid_tabs)
        for tab, (sec_full_name, items) in zip(tabs, sections_data.items()):
            with tab:
                st.write("")
                for item in items:
                    with st.expander(f"Question {item['q_id']} | Trait Detected: {item['label']}"):
                        st.markdown(f"**Scenario:** *{item['question']}*")
                        st.markdown(f"**Your Choice:** `{item['choice_text']}`")
                        st.divider()
                        st.info(f"💡 **Tactical Remediation:** {item['advice']}")
else:
    st.info("No detailed signals logged yet.")


# ==============================================================================
# 7. FOOTER
# ==============================================================================
st.write("")
st.divider()
col_foot1, col_foot2 = st.columns([3, 1])

with col_foot1:
    st.caption("LUMEN Metacognitive Profiler • Runs entirely on your own answers, no external API needed for this page.")

with col_foot2:
    if st.button("Start Over 🔄", use_container_width=True, type="secondary"):
        st.session_state.answers = {}
        if "current_q_idx" in st.session_state:
            st.session_state.current_q_idx = 0
        if "flags" in st.session_state:
            st.session_state.flags["scan_completed"] = False
            st.session_state.flags["chatbot_unlocked"] = False
        st.switch_page("pages/01_Assessment.py")