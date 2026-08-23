import streamlit as st
import re
from core.utils import is_plausible_gemini_key, extract_json_block, extract_text

try:
    from langchain_google_genai import ChatGoogleGenerativeAI
    from langchain_core.messages import HumanMessage
except ImportError:
    st.error("⚠️ CRITICAL FAULT: Missing core dependencies. Execute: pip install langchain langchain-google-genai google-generativeai")
    st.stop()

try:
    from google.api_core import exceptions as google_exceptions
    HAS_GOOGLE_EXCEPTIONS = True
except ImportError:
    HAS_GOOGLE_EXCEPTIONS = False


# ==============================================================================
# 1. ACCESS CONTROL — gated on flags.scan_completed, works with the dev
# shortcut cheat code from 01_Assessment.py as well as a real completed scan.
# ==============================================================================
if not st.session_state.get("flags", {}).get("scan_completed"):
    st.error("🛑 ACCESS DENIED: Neural baseline not established. Complete the diagnostic scan first.")
    if st.button("🚀 Initiate Assessment", type="primary", use_container_width=True):
        st.switch_page("pages/01_Assessment.py")
    st.stop()

user_profile = st.session_state.get("user_profile", {}) or {}
pseudo_raw = user_profile.get("pseudo", "Operator")
pseudo = re.sub(r"[^\w\s\-']", "", str(pseudo_raw)).strip()[:60] or "Operator"

core_vectors = st.session_state.get("core_vectors", {}) or {}


# ==============================================================================
# 2. STYLE
# ==============================================================================
st.markdown("""
<style>
    .roadmap-header {
        background: linear-gradient(90deg, #06B6D4 0%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.3rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="roadmap-header">📅 The Roadmap</p>', unsafe_allow_html=True)
st.write(f"A real, personalized plan for **{pseudo}** — built around your actual rhythm, availability, and what you have to get done, not just 4 generic scores.")
st.divider()

with st.expander("📊 Your cognitive profile (used as a secondary tone modulator, not the main input)"):
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Information Bandwidth", f"{int(core_vectors.get('information_bandwidth', 0))} pts")
    col2.metric("Execution Rigor", f"{int(core_vectors.get('execution_rigor', 0))} pts")
    col3.metric("Chaos Tolerance", f"{int(core_vectors.get('chaos_tolerance', 0))} pts")
    col4.metric("Cognitive Endurance", f"{int(core_vectors.get('cognitive_endurance', 0))} pts")

st.divider()


# ==============================================================================
# 3. SIDEBAR — API KEY & MODEL
# ==============================================================================
with st.sidebar:
    st.markdown("### 🎛️ Engine Control Matrix")
    st.session_state.gemini_api_key = st.text_input(
        "Gemini API Key:",
        value=st.session_state.get("gemini_api_key", ""),
        type="password",
        placeholder="AIzaSy...",
        help=(
            "**How to get your key (free):**\n\n"
            "1. Go to [aistudio.google.com/apikey](https://aistudio.google.com/apikey)\n"
            "2. Sign in with a Google account\n"
            "3. Click **'Create API key'**\n"
            "4. Paste it here (it starts with `AIza...`)\n\n"
            "It's never stored anywhere except in your browser session for this app."
        )
    ).strip()

    selected_model = st.selectbox(
        "Inference Model:",
        options=["gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-3.5-flash"],
        index=0
    )
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

gemini_api_key = st.session_state.get("gemini_api_key", "")


# ==============================================================================
# 4. REAL PERSONALIZATION FORM
# ==============================================================================
st.subheader("🧬 Set up your plan")

with st.form("planning_prefs_form"):
    col_a, col_b = st.columns(2)

    with col_a:
        chronotype = st.selectbox(
            "Your natural rhythm:",
            options=[
                "🌅 Morning person — sharp early, flat by evening",
                "🌙 Night owl — slow to start, sharp late",
                "🔄 It varies a lot day to day",
            ],
        )

        daily_hours = st.slider(
            "How many hours can you realistically give this per day?",
            min_value=1, max_value=10, value=3,
            help="Be honest — a plan based on 8h/day you won't actually do is useless."
        )

        # FIX: max lowered from 21 to 7. A shorter window is both more
        # realistic for a study/work plan and far more reliable for the
        # model to generate correctly-structured JSON for in one shot.
        plan_length = st.slider("Plan length (in days)", 1, 7, 5)

    with col_b:
        preferred_slots = st.multiselect(
            "Time slots you're actually available:",
            options=["Early morning", "Mid-morning", "Afternoon", "Evening", "Late night"],
            default=["Afternoon", "Evening"],
        )

        break_style = st.selectbox(
            "Your break style:",
            options=[
                "Short, frequent breaks (e.g. 5 min every 25 min)",
                "Long, spaced-out breaks (e.g. 30 min after 2h of work)",
                "No strong preference",
            ],
        )

        energy_note = st.selectbox(
            "After a demanding work session, you're usually:",
            options=[
                "Still fired up, I can keep going",
                "Drained, I need a real break",
                "It depends on the topic",
            ],
        )

    tasks_raw = st.text_area(
        "What you actually need to get done in this window (one task per line):",
        placeholder="e.g.\nReview the chapter on sequences for the math test\nMove forward on the scoring module for my app\nPrepare a 30-min presentation for the hackathon",
        height=130,
    )

    deadline_note = st.text_input(
        "A specific deadline to hit within this window? (optional)",
        placeholder="e.g. math test on day 3, hackathon submission on day 7"
    )

    fixed_constraints = st.text_input(
        "Fixed constraints that eat into your time? (optional)",
        placeholder="e.g. classes every morning until 4pm, training on Tuesday and Thursday evenings"
    )

    submitted = st.form_submit_button("Generate My Personalized Plan ⚡", type="primary", use_container_width=True)


# ==============================================================================
# 5. GENERATION
# ==============================================================================
def generate_roadmap(
    pseudo, vectors, api_key, model, timeout, plan_length,
    chronotype, daily_hours, preferred_slots, break_style,
    energy_note, tasks_raw, deadline_note, fixed_constraints,
):
    tasks_block = tasks_raw.strip() if tasks_raw.strip() else "(no specific tasks given — propose generic, realistic progression content)"
    slots_block = ", ".join(preferred_slots) if preferred_slots else "(not specified)"
    deadline_block = deadline_note.strip() if deadline_note.strip() else "(no specific deadline)"
    constraints_block = fixed_constraints.strip() if fixed_constraints.strip() else "(no fixed constraints given)"

    prompt = f"""You are Acumen's planning engine. Build a CONCRETE, REALISTIC execution plan over exactly {plan_length} days for {pseudo}.

[USER'S REAL CONSTRAINTS — TAKE PRIORITY OVER EVERYTHING ELSE]
- Natural rhythm: {chronotype}
- Hours available per day: {daily_hours}h (NEVER exceed this daily budget)
- Actually available time slots: {slots_block}
- Preferred break style: {break_style}
- After an intense session: {energy_note}
- Fixed constraints to respect: {constraints_block}
- Deadline(s) to hit: {deadline_block}

[CONCRETE TASKS TO DISTRIBUTE ACROSS THE PLAN]
{tasks_block}

[SECONDARY MODULATION — cognitive scores 0-100, use ONLY to adjust tone and pacing margin, never to override the constraints above]
- Information Bandwidth: {vectors.get('information_bandwidth', 0)}
- Execution Rigor: {vectors.get('execution_rigor', 0)}
- Chaos Tolerance: {vectors.get('chaos_tolerance', 0)}
- Cognitive Endurance: {vectors.get('cognitive_endurance', 0)}

[RULES]
1. Place the given tasks on specific days, respecting deadlines when given.
2. Never schedule more than the stated daily hour budget.
3. Respect the available time slots and fixed constraints.
4. Build the requested break style directly into the time blocks, not as a separate note.
5. If no specific tasks were given, build generic but realistic progression content consistent with the profile.

Respond with STRICT valid JSON only, no text before or after, in exactly this shape:
{{
  "days": [
    {{
      "day": 1,
      "title": "short day title",
      "blocks": [
        {{"time": "e.g. 5pm-6:30pm", "task": "concrete task", "note": "short note or break type"}}
      ]
    }}
  ]
}}
The "days" array must contain exactly {plan_length} elements, one per day."""

    fallback_chain = [model, "gemini-2.5-flash", "gemini-2.5-flash-lite", "gemini-flash-latest"]
    models_to_try = []
    for m in fallback_chain:
        if m not in models_to_try:
            models_to_try.append(m)

    last_exception = None
    for model_name in models_to_try:
        try:
            llm = ChatGoogleGenerativeAI(
                model=model_name,
                google_api_key=api_key,
                temperature=0.5,
                timeout=timeout,
                max_retries=1,
            )
            response = llm.invoke([HumanMessage(content=prompt)])
            # FIX: response.content isn't guaranteed to be a plain string —
            # it can come back as a list of content blocks, which crashed
            # extract_json_block() downstream ("'list' object has no
            # attribute 'strip'"). Piping it through extract_text() first
            # makes this explicit and matches the pattern used in the other
            # AI pages (Mr. Brown, What If, The Old Days).
            return extract_text(response.content), None
        except Exception as e:
            last_exception = e
            continue

    return None, last_exception


if submitted:
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ Enter a valid Gemini API key in the sidebar before continuing.")
    elif not preferred_slots:
        st.warning("Pick at least one time slot you're available.")
    else:
        with st.spinner("Building your personalized plan..."):
            raw_response, error = generate_roadmap(
                pseudo, core_vectors, gemini_api_key, selected_model, request_timeout,
                plan_length, chronotype, daily_hours, preferred_slots, break_style,
                energy_note, tasks_raw, deadline_note, fixed_constraints,
            )

        if error is not None:
            if HAS_GOOGLE_EXCEPTIONS and isinstance(error, google_exceptions.PermissionDenied):
                st.error("❌ API key rejected. Check that it's correct and active.")
            elif HAS_GOOGLE_EXCEPTIONS and isinstance(error, google_exceptions.ResourceExhausted):
                st.error("❌ Gemini quota exceeded. Try again in a moment.")
            else:
                st.error(f"❌ Generation failed on every available model: {error}")
        else:
            roadmap_data = extract_json_block(raw_response)
            if roadmap_data and isinstance(roadmap_data, dict) and roadmap_data.get("days"):
                st.session_state["roadmap_data"] = roadmap_data
                st.session_state["roadmap_raw"] = None
                st.success("Plan generated successfully!")
            else:
                st.session_state["roadmap_data"] = None
                st.session_state["roadmap_raw"] = raw_response
                st.warning("The plan was generated but the expected JSON format couldn't be parsed — showing raw output below.")


# ==============================================================================
# 6. DISPLAY
# ==============================================================================
roadmap_data = st.session_state.get("roadmap_data")

if roadmap_data:
    st.divider()
    st.subheader("🗺️ Your personalized plan")

    for day in roadmap_data.get("days", []):
        day_num = day.get("day", "?")
        title = day.get("title", "")
        with st.expander(f"Day {day_num} — {title}", expanded=(day_num == 1)):
            blocks = day.get("blocks", [])
            if blocks:
                for block in blocks:
                    time_label = block.get("time", "")
                    task = block.get("task", "")
                    note = block.get("note", "")
                    line = f"**{time_label}** — {task}" if time_label else f"- {task}"
                    st.markdown(line)
                    if note:
                        st.caption(note)
            else:
                for directive in day.get("directives", []):
                    st.markdown(f"- {directive}")

elif st.session_state.get("roadmap_raw"):
    st.divider()
    st.subheader("🗺️ Raw output (unstructured)")
    st.markdown(st.session_state["roadmap_raw"])