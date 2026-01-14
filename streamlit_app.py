import streamlit as st
import time
import streamlit.components.v1 as components

# --- 1. CONFIGURATION (WAJIB DUDUK ATAS SEKALI) ---
st.set_page_config(page_title="ZeroLeak Quiz", page_icon="⚙️", layout="centered")

# --- 2. CUSTOM CSS ---
st.markdown("""
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #000000 100%);
        background-attachment: fixed;
    }
    
    /* Card Style */
    .quiz-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        text-align: center;
        margin-bottom: 20px;
        color: white;
    }
    
    /* Header Center with Gap */
    .header-container {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 20px; /* Jarak antara icon dan teks */
        padding-bottom: 30px;
    }
    
    /* Buttons */
    .stButton button {
        background-color: #FF9F1C;
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
    
    /* Headings */
    h2 { color: #FFFFFF; font-family: 'Arial', sans-serif; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

# --- 3. SIDEBAR WITH 3D MODEL (SIZE DIPERBESAR) ---
with st.sidebar:
    st.markdown("### 🧊 3D Flange Reference")
    
    # URL RAW GITHUB
    glb_url = "https://raw.githubusercontent.com/sqilaf/zeroleak-quiz-app/main/flange.glb"

    # SAYA DAH TUKAR HEIGHT DI SINI KEPADA 450px (LEBIH BESAR)
    html_code = f"""
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/3.0.1/model-viewer.min.js"></script>
    <style>
        model-viewer {{
            width: 100%;
            height: 450px; /* <--- SIZE TINGGI BARU */
            background-color: #262730;
            border-radius: 15px;
            border: 1px solid #444;
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
    # Component frame pun kena besar sikit dari model viewer
    components.html(html_code, height=470)
    
    st.markdown("---")
    st.markdown("### 🏆 Scoreboard")
    if 'score' not in st.session_state: st.session_state.score = 0
    st.write(f"Current Points: **{st.session_state.score}**")
    st.info("Tip: Gunakan model 3D di atas (boleh pusing & zoom) untuk bantu jawab soalan!")

# --- 4. GAME DATA (QUESTIONS) ---
questions = [
    {
        "q": "🛑 SAFETY FIRST: Why loosen the lowest bolt (6 o'clock) first?",
        "options": ["To drain fluid safely (Line of Fire)", "It is easier to reach", "To keep gasket in place"],
        "answer": "To drain fluid safely (Line of Fire)",
        "image": "https://cdn-icons-png.flaticon.com/512/10308/10308976.png"
    },
    {
        "q": "🏷️ TAG CHECK: You see a YELLOW TAG. What is the status?",
        "options": ["Flange is Broken", "Flange is Fully Tightened (Torqued)", "Flange is Leaking"],
        "answer": "Flange is Fully Tightened (Torqued)",
        "image": "https://cdn-icons-png.flaticon.com/512/10698/10698767.png"
    },
    {
        "q": "⚠️ HAZARD ALERT: Which tag color means pipe is NOT sealed?",
        "options": ["Green", "Blue", "Yellow"],
        "answer": "Blue",
        "image": "https://cdn-icons-png.flaticon.com/512/564/564619.png"
    },
    {
        "q": "🔩 TECHNIQUE: Which tightening pattern prevents leaks?",
        "options": ["Clockwise Circle", "Star / Cross Pattern", "Random Pattern"],
        "answer": "Star / Cross Pattern",
        "image": "https://cdn-icons-png.flaticon.com/512/8051/8051388.png"
    },
    {
        "q": "📈 TORQUE STAGES: What are the correct 3 passes?",
        "options": ["10% -> 50% -> 100%", "30% -> 60% -> 100%", "50% -> 75% -> 100%"],
        "answer": "30% -> 60% -> 100%",
        "image": "https://cdn-icons-png.flaticon.com/512/2823/2823933.png"
    },
    {
        "q": "📏 ALIGNMENT: Max allowable gap difference?",
        "options": ["0.8 mm", "2.0 mm", "5.0 mm"],
        "answer": "0.8 mm",
        "image": "https://cdn-icons-png.flaticon.com/512/1684/1684346.png"
    },
    {
        "q": "🛢️ LUBRICATION: Where to apply lube?",
        "options": ["Gasket surface", "Bolt threads & Nut face", "Flange face"],
        "answer": "Bolt threads & Nut face",
        "image": "https://cdn-icons-png.flaticon.com/512/4666/4666497.png"
    },
    {
        "q": "⚙️ GASKET RULE: How to handle the gasket?",
        "options": ["Reuse old gasket", "Use Glue", "Insert NEW gasket"],
        "answer": "Insert NEW gasket",
        "image": "https://cdn-icons-png.flaticon.com/512/3683/3683220.png"
    },
    {
        "q": "🔧 TOOL CHECK: Tool for 'Snug Tight'?",
        "options": ["Hydraulic Wrench", "Hand Spanner", "Impact Gun"],
        "answer": "Hand Spanner",
        "image": "https://cdn-icons-png.flaticon.com/512/2558/2558944.png"
    },
    {
        "q": "✅ FINAL INSPECTION: Tag for 'Leak Proof'?",
        "options": ["Red Tag", "Blue Tag", "Green Tag"],
        "answer": "Green Tag",
        "image": "https://cdn-icons-png.flaticon.com/512/4425/4425788.png"
    }
]

# --- 5. SESSION STATE MANAGEMENT ---
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# --- 6. HEADER BARU (FLANGE ICON + TITLE + WRENCH ICON) ---
st.markdown("""
<div class="header-container">
    <img src="https://cdn-icons-png.flaticon.com/512/8051/8051388.png" width="85">
    
    <h1 style="color:white; margin:0; text-shadow: 2px 2px 4px #000000;">ZEROLEAK QUIZ</h1>
    
    <img src="https://cdn-icons-png.flaticon.com/512/2558/2558944.png" width="85">
</div>
""", unsafe_allow_html=True)

# Progress Bar
if not st.session_state.game_over:
    progress = (st.session_state.current_question / len(questions))
    st.progress(progress)
    st.caption(f"🔧 Question: {st.session_state.current_question + 1}/{len(questions)}")

# --- 7. GAME DISPLAY ---
if not st.session_state.game_over:
    
    q_data = questions[st.session_state.current_question]
    
    # CARD UI
    st.markdown(f"""
    <div class="quiz-card">
        <img src="{q_data['image']}" width="80" style="margin-bottom: 15px; border-radius:10px;">
        <h2>{q_data['q']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # ANSWER FORM
    with st.form(key=f"q_form_{st.session_state.current_question}"):
        user_choice = st.radio("Select Action:", q_data['options'], label_visibility="collapsed")
        submit_btn = st.form_submit_button("CONFIRM CHOICE ➤")
    
    if submit_btn:
        if user_choice == q_data['answer']:
            st.session_state.score += 1
            st.toast("✅ Correct! Good job engineer.", icon="🛠️")
        else:
            st.toast(f"❌ Wrong! Correct: {q_data['answer']}", icon="⚠️")
        
        time.sleep(0.8)
        
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.game_over = True
            st.rerun()

else:
    # RESULT SCREEN
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
