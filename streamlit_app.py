import streamlit as st
import time

import streamlit.components.v1 as components

# ... kod lain ...

# Masukkan kod ini di mana awak nak 3D tu muncul
st.write("### 🧊 3D Flange Preview")

# Gantikan URL_GLB_AWAK dengan link fail glb dari GitHub
# Contoh kod HTML untuk model viewer (Google's component)
html_code = """
<script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.0.1/model-viewer.min.js"></script>
<style>
    model-viewer {
        width: 100%;
        height: 300px;
        background-color: #262730;
        border-radius: 20px;
    }
</style>
<model-viewer 
    src="URL_GLB_AWAK_DI_SINI" 
    alt="A 3D model of a flange" 
    auto-rotate 
    camera-controls>
</model-viewer>
"""

components.html(html_code, height=320)

# --- 1. CONFIGURATION & STYLING ---
st.set_page_config(page_title="ZeroLeak Quiz", page_icon="⚙️", layout="centered")

# Custom CSS untuk UI "Industrial Gaming"
st.markdown("""
    <style>
    /* 1. Background yang lebih hidup (Dark Industrial Gradient) */
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #000000 100%);
        background-attachment: fixed;
    }
    
    /* 2. Card Container Style */
    .quiz-card {
        background: rgba(255, 255, 255, 0.1); /* Glassmorphism effect */
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        text-align: center;
        margin-bottom: 20px;
        color: white;
    }
    
    /* 3. Center Header (Flexbox) */
    .header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
        padding-bottom: 20px;
    }
    
    /* 4. Buttons Design */
    .stButton button {
        background-color: #FF9F1C; /* Industrial Orange */
        color: black;
        width: 100%;
        border-radius: 12px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #FFBF69;
        transform: scale(1.02);
    }
    
    /* Headers inside card */
    h2 {
        color: #FFFFFF;
        font-family: 'Arial', sans-serif;
        font-weight: 700;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. GAME DATA (QUESTIONS) - Updated Icons ---
# Nota: Saya guna link icon yang stabil. Kalau nak tukar, ganti URL dalam "image".
questions = [
    {
        "q": "🛑 SAFETY FIRST: Why loosen the lowest bolt (6 o'clock) first?",
        "options": ["To drain fluid safely (Line of Fire)", "It is easier to reach", "To keep gasket in place"],
        "answer": "To drain fluid safely (Line of Fire)",
        "image": "https://cdn-icons-png.flaticon.com/512/10308/10308976.png" # Industrial Danger Icon
    },
    {
        "q": "🏷️ TAG CHECK: You see a YELLOW TAG. What is the status?",
        "options": ["Flange is Broken", "Flange is Fully Tightened (Torqued)", "Flange is Leaking"],
        "answer": "Flange is Fully Tightened (Torqued)",
        "image": "https://cdn-icons-png.flaticon.com/512/10698/10698767.png" # Tag Icon
    },
    {
        "q": "⚠️ HAZARD ALERT: Which tag color means pipe is NOT sealed?",
        "options": ["Green", "Blue", "Yellow"],
        "answer": "Blue",
        "image": "https://cdn-icons-png.flaticon.com/512/564/564619.png" # Alert Triangle
    },
    {
        "q": "🔩 TECHNIQUE: Which tightening pattern prevents leaks?",
        "options": ["Clockwise Circle", "Star / Cross Pattern", "Random Pattern"],
        "answer": "Star / Cross Pattern",
        "image": "https://cdn-icons-png.flaticon.com/512/8051/8051388.png" # Flange Bolt Icon
    },
    {
        "q": "📈 TORQUE STAGES: What are the correct 3 passes?",
        "options": ["10% -> 50% -> 100%", "30% -> 60% -> 100%", "50% -> 75% -> 100%"],
        "answer": "30% -> 60% -> 100%",
        "image": "https://cdn-icons-png.flaticon.com/512/2823/2823933.png" # Stats/Levels Icon
    },
    {
        "q": "📏 ALIGNMENT: Max allowable gap difference?",
        "options": ["0.8 mm", "2.0 mm", "5.0 mm"],
        "answer": "0.8 mm",
        "image": "https://cdn-icons-png.flaticon.com/512/1684/1684346.png" # Caliper/Measure Icon
    },
    {
        "q": "🛢️ LUBRICATION: Where to apply lube?",
        "options": ["Gasket surface", "Bolt threads & Nut face", "Flange face"],
        "answer": "Bolt threads & Nut face",
        "image": "https://cdn-icons-png.flaticon.com/512/4666/4666497.png" # Lubricant/Oil Drop
    },
    {
        "q": "⚙️ GASKET RULE: How to handle the gasket?",
        "options": ["Reuse old gasket", "Use Glue", "Insert NEW gasket"],
        "answer": "Insert NEW gasket",
        "image": "https://cdn-icons-png.flaticon.com/512/3683/3683220.png" # Gasket/Part Icon
    },
    {
        "q": "🔧 TOOL CHECK: Tool for 'Snug Tight'?",
        "options": ["Hydraulic Wrench", "Hand Spanner", "Impact Gun"],
        "answer": "Hand Spanner",
        "image": "https://cdn-icons-png.flaticon.com/512/2558/2558944.png" # Wrench Icon
    },
    {
        "q": "✅ FINAL INSPECTION: Tag for 'Leak Proof'?",
        "options": ["Red Tag", "Blue Tag", "Green Tag"],
        "answer": "Green Tag",
        "image": "https://cdn-icons-png.flaticon.com/512/4425/4425788.png" # Certified/Check Icon
    }
]

# --- 3. SESSION STATE MANAGEMENT ---
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# --- 4. HEADER (CENTERED) ---
# Menggunakan HTML Flexbox untuk center align icon dan text
st.markdown("""
<div class="header-container">
    <img src="https://cdn-icons-png.flaticon.com/512/6009/6009864.png" width="80">
    <h1 style="color:white; margin:0;">ZEROLEAK QUIZ</h1>
</div>
""", unsafe_allow_html=True)

# Progress Bar
if not st.session_state.game_over:
    progress = (st.session_state.current_question / len(questions))
    st.progress(progress)
    st.caption(f"🔧 Question: {st.session_state.current_question + 1}/{len(questions)}")

# --- 5. GAME DISPLAY ---
if not st.session_state.game_over:
    
    # Get current question data
    q_data = questions[st.session_state.current_question]
    
    # === THE CARD UI ===
    st.markdown(f"""
    <div class="quiz-card">
        <img src="{q_data['image']}" width="80" style="margin-bottom: 15px; border-radius:10px;">
        <h2>{q_data['q']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Answer Buttons
    with st.form(key=f"q_form_{st.session_state.current_question}"):
        user_choice = st.radio("Select Action:", q_data['options'], label_visibility="collapsed")
        submit_btn = st.form_submit_button("CONFIRM CHOICE ➤")
    
    if submit_btn:
        # Check Answer
        if user_choice == q_data['answer']:
            st.session_state.score += 1
            st.toast("✅ Correct! Good job engineer.", icon="🛠️")
        else:
            st.toast(f"❌ Wrong! Correct: {q_data['answer']}", icon="⚠️")
        
        # Delay slightly for effect
        time.sleep(0.8)
        
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.game_over = True
            st.rerun()

else:
    # === GAME OVER / RESULT SCREEN ===
    score = st.session_state.score
    st.markdown("---")
    
    if score >= 8:
        st.balloons()
        st.markdown(f"""
        <div class="quiz-card" style="border: 2px solid #00FF00;">
            <img src="https://cdn-icons-png.flaticon.com/512/7518/7518748.png" width="100">
            <h1 style="color: #00FF00;">COMPETENCY CERTIFIED</h1>
            <h2>Score: {score}/10</h2>
            <p>You have successfully demonstrated the theoretical knowledge.</p>
            <p><strong>Status: SITE READY</strong></p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="quiz-card" style="border: 2px solid #FF0000;">
            <img src="https://cdn-icons-png.flaticon.com/512/497/497738.png" width="100">
            <h1 style="color: #FF0000;">TRAINING REQUIRED</h1>
            <h2>Score: {score}/10</h2>
            <p>Your score is below the safety threshold.</p>
            <p>Please review the AR module and try again.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("🔄 RETAKE QUIZ"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()

# --- SIDEBAR ---
with st.sidebar:
    st.markdown("### 🏆 Scoreboard")
    st.write(f"Current Points: **{st.session_state.score}**")
    st.markdown("---")
    st.info("Remember: AR helps you visualize, VR helps you practice, and this Quiz certifies your knowledge.")
