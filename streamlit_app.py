import streamlit as st
import time
import streamlit.components.v1 as components

# --- 1. CONFIGURATION (MUST BE TOP) ---
st.set_page_config(page_title="ZeroLeak Quiz", page_icon="⚙️", layout="centered")

# --- 2. CUSTOM CSS (STYLING) ---
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #000000 100%);
        background-attachment: fixed;
    }
    
    /* Card Style (Glassmorphism) */
    .quiz-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 40px;
        border-radius: 15px;
        box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 20px;
        color: white;
        text-align: left; /* Align text left for better reading */
    }
    
    /* Header Style */
    .main-header {
        text-align: center;
        color: white;
        font-family: 'Helvetica', sans-serif;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 10px;
    }
    
    /* Button Style */
    .stButton button {
        background-color: #FF9F1C;
        color: black;
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        border: none;
        padding: 12px;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #FFBF69;
        transform: scale(1.01);
    }
    
    /* Question Text */
    h2 {
        color: #FFFFFF;
        font-family: 'Arial', sans-serif;
        font-weight: 600;
        font-size: 24px;
        margin-top: 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR (3D MODEL & INFO) ---
with st.sidebar:
    st.markdown("### 🧊 3D Flange Reference")
    
    # URL RAW GITHUB
    glb_url = "https://raw.githubusercontent.com/sqilaf/zeroleak-quiz-app/main/flange.glb"

    # HEIGHT DIUBAH KE 280px (LEBIH RENDAH/LEBAR)
    html_code = f"""
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.0.1/model-viewer.min.js"></script>
    <style>
        model-viewer {{
            width: 100%;
            height: 280px; /* SIZE BARU: LEBAR (Landscape) */
            background-color: #262730;
            border-radius: 10px;
            border: 1px solid #555;
        }}
    </style>
    <model-viewer 
        src="{glb_url}" 
        alt="A 3D model of a flange" 
        auto-rotate 
        camera-controls
        shadow-intensity="1">
    </model-viewer>
    """
    components.html(html_code, height=300)
    
    st.markdown("---")
    # AYAT ASAL KEMBALI
    st.info("Remember: AR helps you visualize, VR helps you practice, and this Quiz certifies your knowledge.")
    
    st.markdown("---")
    if 'score' not in st.session_state: st.session_state.score = 0
    st.write(f"Current Score: **{st.session_state.score}**")

# --- 4. GAME DATA (QUESTIONS) ---
# I removed the 'image' key and added 'icon' directly to the question text
questions = [
    {
        "q": "🛑 SAFETY FIRST: Why loosen the lowest bolt (6 o'clock) first?",
        "options": ["To drain fluid safely (Line of Fire)", "It is easier to reach", "To keep gasket in place"],
        "answer": "To drain fluid safely (Line of Fire)"
    },
    {
        "q": "🏷️ TAG CHECK: You see a YELLOW TAG. What is the status?",
        "options": ["Flange is Broken", "Flange is Fully Tightened (Torqued)", "Flange is Leaking"],
        "answer": "Flange is Fully Tightened (Torqued)"
    },
    {
        "q": "⚠️ HAZARD ALERT: Which tag color means pipe is NOT sealed?",
        "options": ["Green", "Blue", "Yellow"],
        "answer": "Blue"
    },
    {
        "q": "⚙️ TECHNIQUE: Which tightening pattern prevents leaks?",
        "options": ["Clockwise Circle", "Star / Cross Pattern", "Random Pattern"],
        "answer": "Star / Cross Pattern"
    },
    {
        "q": "📈 TORQUE STAGES: What are the correct 3 passes?",
        "options": ["10% -> 50% -> 100%", "30% -> 60% -> 100%", "50% -> 75% -> 100%"],
        "answer": "30% -> 60% -> 100%"
    },
    {
        "q": "📏 ALIGNMENT: Max allowable gap difference?",
        "options": ["0.8 mm", "2.0 mm", "5.0 mm"],
        "answer": "0.8 mm"
    },
    {
        "q": "🛢️ LUBRICATION: Where to apply lube?",
        "options": ["Gasket surface", "Bolt threads & Nut face", "Flange face"],
        "answer": "Bolt threads & Nut face"
    },
    {
        "q": "🧩 GASKET RULE: How to handle the gasket?",
        "options": ["Reuse old gasket", "Use Glue", "Insert NEW gasket"],
        "answer": "Insert NEW gasket"
    },
    {
        "q": "🔧 TOOL CHECK: Tool for 'Snug Tight'?",
        "options": ["Hydraulic Wrench", "Hand Spanner", "Impact Gun"],
        "answer": "Hand Spanner"
    },
    {
        "q": "✅ FINAL INSPECTION: Tag for 'Leak Proof'?",
        "options": ["Red Tag", "Blue Tag", "Green Tag"],
        "answer": "Green Tag"
    }
]

# --- 5. SESSION STATE MANAGEMENT ---
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# --- 6. HEADER (CLEAN & SIMPLE) ---
# Menggunakan emoji terus dalam teks supaya pasti keluar
st.markdown("<div class='main-header'><h1>🛠️ ZEROLEAK QUIZ 🛠️</h1></div>", unsafe_allow_html=True)

# Progress Bar
if not st.session_state.game_over:
    progress = (st.session_state.current_question / len(questions))
    st.progress(progress)
    st.caption(f"Question {st.session_state.current_question + 1} of {len(questions)}")

# --- 7. GAME DISPLAY ---
if not st.session_state.game_over:
    
    q_data = questions[st.session_state.current_question]
    
    # CARD UI (TANPA GAMBAR BESAR, CUMA SOALAN)
    st.markdown(f"""
    <div class="quiz-card">
        <h2>{q_data['q']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # ANSWER FORM
    with st.form(key=f"q_form_{st.session_state.current_question}"):
        user_choice = st.radio("Select Answer:", q_data['options'], label_visibility="collapsed")
        st.markdown("<br>", unsafe_allow_html=True) # Spacer
        submit_btn = st.form_submit_button("CONFIRM CHOICE ➤")
    
    if submit_btn:
        if user_choice == q_data['answer']:
            st.session_state.score += 1
            st.toast("✅ Correct!", icon="👍")
        else:
            st.toast(f"❌ Wrong! Correct: {q_data['answer']}", icon="⚠️")
        
        time.sleep(0.5)
        
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.game_over = True
            st.rerun()

else:
    # RESULT SCREEN
    final_score = st.session_state.score
    st.markdown("---")
    
    if final_score >= 8:
        st.balloons()
        st.markdown(f"""
        <div class="quiz-card" style="border: 2px solid #00FF00; text-align: center;">
            <h1 style="color: #00FF00;">COMPETENCY CERTIFIED</h1>
            <h2>Score: {final_score}/10</h2>
            <p>You are now SITE READY.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="quiz-card" style="border: 2px solid #FF0000; text-align: center;">
            <h1 style="color: #FF0000;">TRAINING REQUIRED</h1>
            <h2>Score: {final_score}/10</h2>
            <p>Please review the AR module.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("🔄 RETAKE QUIZ"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()
