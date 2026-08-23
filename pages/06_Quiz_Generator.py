import streamlit as st
from core.utils import is_plausible_gemini_key, extract_json_block, extract_text
import pypdf

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

# FIX: added PDF support. pypdf must be in requirements.txt for this to work
# once deployed — see the note at the end of this file.
try:
    from pypdf import PdfReader
    HAS_PDF_SUPPORT = True
except ImportError:
    HAS_PDF_SUPPORT = False


# ==============================================================================
# 1. STYLE
# ==============================================================================
st.markdown("""
<style>
    .quiz-header {
        background: linear-gradient(90deg, #8B5CF6 0%, #06B6D4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 2.3rem;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="quiz-header">🧩 Quiz Forge</p>', unsafe_allow_html=True)
st.write("Drop in your notes, a course PDF, or paste text directly — Acumen turns it into a graded quiz on the spot.")
st.divider()


# ==============================================================================
# 2. SIDEBAR — API KEY & MODEL
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
        index=0,
        help="gemini-2.5-flash is the best balance of quality and reliability."
    )

    num_questions = st.slider("Number of questions", 3, 15, 5, 1)
    request_timeout = st.slider("Request Timeout (s)", 10, 120, 45, 5)

gemini_api_key = st.session_state.get("gemini_api_key", "")


# ==============================================================================
# 3. SOURCE CONTENT INPUT
# ==============================================================================
accepted_types = ["txt", "md"]
if HAS_PDF_SUPPORT:
    accepted_types.append("pdf")
else:
    st.warning("⚠️ PDF support isn't available right now (missing `pypdf` dependency) — only .txt and .md files work. Text pasting below still works regardless.")

uploaded_file = st.file_uploader(
    f"Drop a file ({', '.join(t.upper() for t in accepted_types)})",
    type=accepted_types
)
raw_text = st.text_area("Or paste your content directly here:", height=200)


def extract_pdf_text(file) -> str:
    """Extract text from an uploaded PDF using pypdf. Returns '' on failure
    rather than raising, so a corrupt/scanned PDF doesn't crash the page."""
    try:
        reader = PdfReader(file)
        pages_text = []
        for page in reader.pages:
            page_text = page.extract_text() or ""
            if page_text.strip():
                pages_text.append(page_text)
        return "\n\n".join(pages_text)
    except Exception:
        return ""


content = ""
if uploaded_file is not None:
    file_name = uploaded_file.name.lower()
    if file_name.endswith(".pdf"):
        if not HAS_PDF_SUPPORT:
            st.error("PDF support isn't installed on this deployment. Try a .txt or .md file, or paste the text instead.")
        else:
            with st.spinner("Extracting text from PDF..."):
                content = extract_pdf_text(uploaded_file)
            if not content.strip():
                st.error("Couldn't extract any text from this PDF — it might be a scanned image rather than real text. Try pasting the text manually instead.")
    else:
        try:
            content = uploaded_file.read().decode("utf-8", errors="ignore")
        except Exception:
            st.error("Couldn't read this file. Make sure it's a valid text file.")
elif raw_text:
    content = raw_text.strip()

# FIX: limit raised from 12,000 to 40,000 characters (~8-10k words) — the
# previous limit was too small for a real course PDF, which was the main
# complaint. Gemini's context window comfortably handles this; the limit
# here is mainly to keep prompt cost and latency reasonable, not a hard
# model constraint.
MAX_CHARS = 40000
if len(content) > MAX_CHARS:
    st.warning(f"Content exceeds {MAX_CHARS:,} characters — only the beginning will be used to generate the quiz.")
    content = content[:MAX_CHARS]

if content:
    word_count = len(content.split())
    st.caption(f"📄 {word_count:,} words loaded and ready.")


# ==============================================================================
# 4. QUIZ GENERATION (with model fallback, same pattern as other AI pages)
# ==============================================================================
def generate_quiz(source_text: str, api_key: str, model: str, timeout: int, n_questions: int):
    prompt = f"""From the following text, generate exactly {n_questions} multiple-choice questions (MCQ) that test real comprehension of the material, not just superficial detail recall.

Respond with STRICT valid JSON only, no text before or after, in exactly this shape:
{{
  "questions": [
    {{
      "question": "question text",
      "options": {{"A": "...", "B": "...", "C": "...", "D": "..."}},
      "correct": "A",
      "explanation": "short explanation of the correct answer"
    }}
  ]
}}

TEXT:
{source_text}"""

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
                temperature=0.4,
                timeout=timeout,
                max_retries=1,
            )
            response = llm.invoke([HumanMessage(content=prompt)])
            # FIX: response.content isn't guaranteed to be a plain string —
            # piping through extract_text() first avoids the
            # "'list' object has no attribute 'strip'" crash seen before.
            return extract_text(response.content), None
        except Exception as e:
            last_exception = e
            continue

    return None, last_exception


if st.button("Generate Quiz 🚀", type="primary", use_container_width=True):
    if not is_plausible_gemini_key(gemini_api_key):
        st.error("⚠️ Enter a valid Gemini API key in the sidebar before continuing.")
    elif not content:
        st.warning("Provide some text or a file before generating the quiz.")
    else:
        with st.spinner("Analyzing content and generating questions..."):
            raw_response, error = generate_quiz(content, gemini_api_key, selected_model, request_timeout, num_questions)

        if error is not None:
            if HAS_GOOGLE_EXCEPTIONS and isinstance(error, google_exceptions.PermissionDenied):
                st.error("❌ API key rejected. Check that it's correct and active.")
            elif HAS_GOOGLE_EXCEPTIONS and isinstance(error, google_exceptions.ResourceExhausted):
                st.error("❌ Gemini quota exceeded. Try again in a moment.")
            else:
                st.error(f"❌ Generation failed on every available model: {error}")
        else:
            quiz_data = extract_json_block(raw_response)
            if quiz_data and isinstance(quiz_data, dict) and quiz_data.get("questions"):
                st.session_state["generated_quiz_data"] = quiz_data
                st.session_state["quiz_answers"] = {}
                st.session_state["quiz_graded"] = False
                st.session_state["generated_quiz_raw"] = None
                st.success("Quiz generated successfully!")
            else:
                st.session_state["generated_quiz_data"] = None
                st.session_state["generated_quiz_raw"] = raw_response
                st.warning("The quiz was generated but the expected JSON format couldn't be parsed — showing raw output below.")


# ==============================================================================
# 5. INTERACTIVE QUIZ DISPLAY
# ==============================================================================
quiz_data = st.session_state.get("generated_quiz_data")

if quiz_data:
    st.divider()
    st.subheader("📝 Your Quiz")

    questions = quiz_data.get("questions", [])
    quiz_answers = st.session_state.setdefault("quiz_answers", {})

    for i, q in enumerate(questions):
        st.markdown(f"**Q{i + 1}. {q.get('question', '')}**")
        options = q.get("options", {})
        option_keys = list(options.keys())

        selected = st.radio(
            f"question_{i}",
            options=option_keys,
            format_func=lambda k, opts=options: f"{k}) {opts.get(k, '')}",
            index=None,
            key=f"quiz_radio_{i}",
            label_visibility="collapsed"
        )
        quiz_answers[i] = selected
        st.write("")

    if st.button("Check Answers ✅", use_container_width=True):
        st.session_state["quiz_graded"] = True

    if st.session_state.get("quiz_graded"):
        score = 0
        for i, q in enumerate(questions):
            correct = q.get("correct")
            user_answer = quiz_answers.get(i)
            if user_answer == correct:
                score += 1
                st.success(f"Q{i + 1}: Correct ✅ — {q.get('explanation', '')}")
            else:
                st.error(f"Q{i + 1}: Incorrect ❌ — Correct answer: {correct}) {q.get('options', {}).get(correct, '')}. {q.get('explanation', '')}")

        st.metric("Final Score", f"{score} / {len(questions)}")

elif st.session_state.get("generated_quiz_raw"):
    st.divider()
    st.subheader("📝 Raw output (unstructured)")
    st.markdown(st.session_state["generated_quiz_raw"])