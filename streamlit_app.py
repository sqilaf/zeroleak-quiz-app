import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ZeroLeak Assessment",
    page_icon="🛠️",
    layout="centered"
)

# --- SIDEBAR INFO ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/10329/10329486.png", width=100)
    st.title("Project ZeroLeak")
    st.markdown("### 🎓 Training Flow")
    st.info("1️⃣ **AR Mode**: Learn the Theory")
    st.info("2️⃣ **VR Mode**: Simulate the Job")
    st.info("3️⃣ **Web Quiz**: Test Competency")
    st.warning("This assessment is optional but recommended to certify your knowledge.")

# --- MAIN HEADER ---
st.title("🛠️ ZeroLeak: Competency Check")
st.caption("Post-Training Assessment for Flange Management System")
st.markdown("---")

st.write("""
**Instructions:** Please complete this quiz **AFTER** experiencing the AR Learning Module and VR Simulation. 
You need to score at least **8/10** to be considered 'Site Ready'.
""")

# --- QUIZ FORM ---
with st.form("quiz_form"):
    
    # QUESTION 1
    st.subheader("1. Safety First (Line of Fire)")
    st.write("When disassembling a flange, why must you loosen the **lowest bolt (6 o'clock)** first?")
    q1 = st.radio(
        "Select the best reason:",
        ("It is the easiest bolt to reach.",
         "To allow trapped fluid to drain downwards, away from your body.",
         "To keep the gasket from falling out."),
        key="q1"
    )

    # QUESTION 2
    st.subheader("2. Tagging System (Status)")
    st.write("You see a **YELLOW TAG** on a flange joint. What does this indicate?")
    q2 = st.radio(
        "Identify the status:",
        ("Flange is Broken / Disassembled.",
         "Flange is Hand Tightened only.",
         "Flange is Fully Tightened (Torqued)."),
        key="q2"
    )

    # QUESTION 3
    st.subheader("3. Tagging System (Danger)")
    st.write("Which tag color indicates that the pipe is **NOT SEALED** and dangerous?")
    q3 = st.radio(
        "Select the color:",
        ("🟢 Green", "🔵 Blue", "🟡 Yellow"),
        key="q3"
    )

    # QUESTION 4
    st.subheader("4. Torque Sequence")
    st.write("To prevent uneven pressure and leaks, which tightening pattern must be used?")
    q4 = st.radio(
        "Select the pattern:",
        ("Circular Pattern (Clockwise)",
         "Star / Cross Pattern",
         "Random Pattern"),
        key="q4"
    )

    # QUESTION 5
    st.subheader("5. Torque Application Stages")
    st.write("According to the procedure, what are the correct **three passes** for torque tightening?")
    q5 = st.radio(
        "Select the percentage sequence:",
        ("10% ➝ 50% ➝ 100%",
         "30% ➝ 60% ➝ 100%",
         "50% ➝ 75% ➝ 100%"),
        key="q5"
    )

    # QUESTION 6
    st.subheader("6. Alignment Check")
    st.write("Before inserting bolts, the flange faces must be parallel. What is the **maximum allowable gap difference**?")
    q6 = st.radio(
        "Select the value:",
        ("0.8 mm", "2.0 mm", "5.0 mm"),
        key="q6"
    )

    # QUESTION 7
    st.subheader("7. Lubrication")
    st.write("Where should the lubricant be applied on the fasteners?")
    q7 = st.radio(
        "Select the correct location:",
        ("On the gasket surface only.",
         "On the bolt threads and the face of the nuts.",
         "On the flange face."),
        key="q7"
    )

    # QUESTION 8
    st.subheader("8. Gasket Installation")
    st.write("During assembly (Step 3), how should you handle the gasket?")
    q8 = st.radio(
        "Select the correct action:",
        ("Reuse the old gasket to save cost.",
         "Apply glue to the gasket to hold it.",
         "Insert a NEW gasket and let it rest on the bottom bolts."),
        key="q8"
    )

    # QUESTION 9
    st.subheader("9. Snug Tightening")
    st.write("In Step 4 (Snug Tight), which tool should you use?")
    q9 = st.radio(
        "Select the tool:",
        ("Hydraulic Torque Wrench.",
         "Hand or Standard Spanner/Wrench.",
         "Impact Gun."),
        key="q9"
    )

    # QUESTION 10
    st.subheader("10. Final Verification")
    st.write("After the pressure test is passed (Leak Proof), which tag is applied?")
    q10 = st.radio(
        "Select the final tag:",
        ("🔴 Red Tag", "🔵 Blue Tag", "🟢 Green Tag"),
        key="q10"
    )

    st.markdown("---")
    submitted = st.form_submit_button("Submit Assessment")

# --- SCORING LOGIC ---
if submitted:
    score = 0
    
    # Marking Scheme (Based on provided images/PDF)
    if q1 == "To allow trapped fluid to drain downwards, away from your body.": score += 1
    if q2 == "Flange is Fully Tightened (Torqued).": score += 1
    if q3 == "🔵 Blue": score += 1
    if q4 == "Star / Cross Pattern": score += 1
    if q5 == "30% ➝ 60% ➝ 100%": score += 1
    if q6 == "0.8 mm": score += 1
    if q7 == "On the bolt threads and the face of the nuts.": score += 1
    if q8 == "Insert a NEW gasket and let it rest on the bottom bolts.": score += 1
    if q9 == "Hand or Standard Spanner/Wrench.": score += 1
    if q10 == "🟢 Green Tag": score += 1

    # --- RESULT DISPLAY ---
    st.subheader("Assessment Result")
    my_bar = st.progress(0)
    
    # Animation for score
    score_percent = int((score / 10) * 100)
    my_bar.progress(score_percent)

    if score >= 8:
        st.success(f"🎉 EXCELLENT! You scored {score}/10.")
        st.balloons()
        st.write("You have demonstrated strong knowledge of the Flange Management System.")
    elif score >= 5:
        st.warning(f"⚠️ GOOD EFFORT. You scored {score}/10.")
        st.write("You might want to review the AR module for specific torque procedures.")
    else:
        st.error(f"❌ PLEASE REVIEW. You scored {score}/10.")
        st.write("Please revisit the AR Learning Module and try again.")

    # Expandable Answer Key (For learning purposes)
    with st.expander("View Correct Answers (For Revision)"):
        st.markdown("""
        1. [cite_start]**Line of Fire**: Drain fluid away from body[cite: 1544].
        2. **Yellow Tag**: Fully Torqued.
        3. **Blue Tag**: Broken/Open (Dangerous).
        4. **Pattern**: Star/Cross Pattern.
        5. [cite_start]**Stages**: 30% -> 60% -> 100%[cite: 1544].
        6. [cite_start]**Gap**: Max 0.8 mm[cite: 1544].
        7. [cite_start]**Lube**: Threads and Nut Face[cite: 1544].
        8. [cite_start]**Gasket**: Use New Gasket[cite: 1544].
        9. [cite_start]**Snug**: Hand/Standard Wrench[cite: 1544].
        10. **Green Tag**: Leak Proof/Tested.
        """)
