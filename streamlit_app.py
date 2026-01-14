import streamlit as st
import time

# --- 1. CONFIGURATION & STYLING ---
st.set_page_config(page_title="ZeroLeak Quest", page_icon="🎮", layout="centered")

# Custom CSS untuk jadikan UI nampak macam "Game Card"
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #0E1117;
    }
    
    /* Card Container Style */
    .quiz-card {
        background-color: #262730;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        border: 2px solid #4B4B4B;
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Progress Bar Color */
    .stProgress > div > div > div > div {
        background-color: #00FF00;
    }
    
    /* Buttons */
    .stButton button {
        width: 100%;
        border-radius: 10px;
        font-weight: bold;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    
    /* Headers inside card */
    h2 {
        color: #FFFFFF;
        text-shadow: 0 0 10px #000000;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. GAME DATA (QUESTIONS) ---
questions = [
    {
        "q": "🛑 SAFETY CHECK: Why loosen the lowest bolt (6 o'clock) first?",
        "options": ["To drain fluid safely (Line of Fire)", "It is easier to reach", "To keep gasket in place"],
        "answer": "To drain fluid safely (Line of Fire)",
        "image": "https://cdn-icons-png.flaticon.com/512/1165/1165674.png" # Safety Icon
    },
    {
        "q": "🏷️ STATUS CHECK: You see a YELLOW TAG. What does it mean?",
        "options": ["Flange is Broken", "Flange is Fully Tightened (Torqued)", "Flange is Leaking"],
        "answer": "Flange is Fully Tightened (Torqued)",
        "image": "https://cdn-icons-png.flaticon.com/512/2680/2680903.png" # Tag Icon
    },
    {
        "q": "⚠️ DANGER ZONE: Which tag color means pipe is NOT sealed?",
        "options": ["Green", "Blue", "Yellow"],
        "answer": "Blue",
        "image": "https://cdn-icons-png.flaticon.com/512/564/564619.png" # Danger Icon
    },
    {
        "q": "🔩 TECHNIQUE: Which tightening pattern prevents leaks?",
        "options": ["Clockwise Circle", "Star / Cross Pattern", "Random Pattern"],
        "answer": "Star / Cross Pattern",
        "image": "https://cdn-icons-png.flaticon.com/512/3756/3756748.png" # Bolt Icon
    },
    {
        "q": "📈 TORQUE STAGES: What are the correct 3 passes?",
        "options": ["10% -> 50% -> 100%", "30% -> 60% -> 100%", "50% -> 75% -> 100%"],
        "answer": "30% -> 60% -> 100%",
        "image": "https://cdn-icons-png.flaticon.com/512/8061/8061614.png" # Chart Icon
    },
    {
        "q": "📐 ALIGNMENT: Max allowable gap difference?",
        "options": ["0.8 mm", "2.0 mm", "5.0 mm"],
        "answer": "0.8 mm",
        "image": "https://cdn-icons-png.flaticon.com/512/12603/12603780.png" # Ruler Icon
    },
    {
        "q": "💧 LUBRICATION: Where to apply lube?",
        "options": ["Gasket surface", "Bolt threads & Nut face", "Flange face"],
        "answer": "Bolt threads & Nut face",
        "image": "https://cdn-icons-png.flaticon.com/512/3079/3079172.png" # Oil Icon
    },
    {
        "q": "🧩 GASKET RULE: How to handle the gasket?",
        "options": ["Reuse old gasket", "Use Glue", "Insert NEW gasket"],
        "answer": "Insert NEW gasket",
        "image": "https://cdn-icons-png.flaticon.com/512/9364/9364803.png" # Gasket Icon
    },
    {
        "q": "🔧 TOOL CHECK: Tool for 'Snug Tight'?",
        "options": ["Hydraulic Wrench", "Hand Spanner", "Impact Gun"],
        "answer": "Hand Spanner",
        "image": "https://cdn-icons-png.flaticon.com/512/2558/2558944.png" # Wrench Icon
    },
    {
        "q": "✅ FINAL CHECK: Tag for 'Leak Proof'?",
        "options": ["Red Tag", "Blue Tag", "Green Tag"],
        "answer": "Green Tag",
        "image": "https://cdn-icons-png.flaticon.com/512/190/190411.png" # Check Icon
    }
]

# --- 3. SESSION STATE MANAGEMENT ---
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# --- 4. GAME LOGIC ---

# Header Logo
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/10329/10329486.png", width=80)
    st.markdown("<h1 style='text-align: center; margin-top: -10px;'>ZeroLeak Quest</h1>", unsafe_allow_html=True)

# Progress Bar
if not st.session_state.game_over:
    progress = (st.session_state.current_question / len(questions))
    st.progress(progress)
    st.caption(f"Mission Progress: {st.session_state.current_question + 1}/{len(questions)}")

# --- DISPLAY CARD OR RESULT ---
if not st.session_state.game_over:
    
    # Get current question data
    q_data = questions[st.session_state.current_question]
    
    # === THE CARD UI ===
    st.markdown(f"""
    <div class="quiz-card">
        <img src="{q_data['image']}" width="60" style="margin-bottom: 10px;">
        <h2>{q_data['q']}</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Answer Buttons
    # We use a form to group the radio button and submit
    with st.form(key=f"q_form_{st.session_state.current_question}"):
        user_choice = st.radio("Choose your action:", q_data['options'], label_visibility="collapsed")
        submit_btn = st.form_submit_button("LOCK ANSWER 🔒")
    
    if submit_btn:
        # Check Answer
        if user_choice == q_data['answer']:
            st.session_state.score += 1
            st.toast("✅ Correct! System Secure.", icon="🛡️")
        else:
            st.toast(f"❌ Wrong! Correct: {q_data['answer']}", icon="⚠️")
        
        # Delay slightly for effect then move next
        time.sleep(0.5)
        
        if st.session_state.current_question < len(questions) - 1:
            st.session_state.current_question += 1
            st.rerun()
        else:
            st.session_state.game_over = True
            st.rerun()

else:
    # === GAME OVER SCREEN ===
    score = st.session_state.score
    st.markdown("---")
    
    if score >= 8:
        st.balloons()
        st.markdown(f"""
        <div class="quiz-card" style="border-color: #00FF00;">
            <h1>🏆 MISSION ACCOMPLISHED</h1>
            <h2 style="color: #00FF00;">Score: {score}/10</h2>
            <p>You are certified for VR Simulation!</p>
            <h1>ACCESS CODE: <span style="background-color: #333; padding: 5px 15px; border-radius: 5px;">8829</span></h1>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="quiz-card" style="border-color: #FF0000;">
            <h1>⚠️ MISSION FAILED</h1>
            <h2 style="color: #FF0000;">Score: {score}/10</h2>
            <p>Safety standards not met. Please review AR Training.</p>
        </div>
        """, unsafe_allow_html=True)
    
    if st.button("🔄 RESTART MISSION"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.game_over = False
        st.rerun()

# --- SIDEBAR (Context) ---
with st.sidebar:
    st.title("Project ZeroLeak")
    st.markdown("---")
    st.write("Current Score:")
    st.metric(label="Points", value=st.session_state.score)
    st.markdown("---")
    st.info("💡 Tip: Review the AR diagrams if you get stuck!")
