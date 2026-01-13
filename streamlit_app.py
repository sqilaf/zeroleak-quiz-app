import streamlit as st

# Setup Halaman
st.set_page_config(page_title="ZeroLeak Training Assessment", page_icon="🛢️")

# Tajuk Utama
st.title("🛢️ ZeroLeak: Flange Assessment Quiz")
st.write("Sila jawab semua soalan sebelum memasuki simulasi VR.")
st.markdown("---")

# Menggunakan Form supaya page tak reload setiap kali tekan
with st.form("quiz_form"):
    
    # --- SOALAN 1: SAFETY (Berdasarkan PDF Page 21) ---
    st.subheader("1. Keselamatan (Safety Disassembly)")
    st.write("Mengapakah bolt pada bahagian bawah (pukul 6) perlu dilonggarkan dahulu?")
    q1 = st.radio(
        "Pilih jawapan yang tepat:",
        ("Supaya gasket tidak jatuh", 
         "Untuk mengalirkan sisa cecair ke bawah & elak terkena badan (Line of Fire)", 
         "Kerana ia paling mudah dicapai"),
        key="q1"
    )

    # --- SOALAN 2: TAGGING (Berdasarkan Gambar AR & PDF Page 20) ---
    st.subheader("2. Sistem Tagging (Flange Status)")
    st.write("Selepas flange siap dipasang dan diketatkan (torqued), tag warna apakah yang perlu digantung?")
    q2 = st.radio(
        "Rujuk Sistem Tagging:",
        ("🔵 Biru (Flange Broken)", 
         "🔴 Merah (Flange Assembled - Hand Tight)", 
         "🟡 Kuning (Flange Tightened - Torqued)"),
        key="q2"
    )

    # --- SOALAN 3: TORQUE SEQUENCE (Berdasarkan Gambar AR Cross Pattern) ---
    st.subheader("3. Teknik Pemasangan")
    st.write("Apakah corak (pattern) yang MESTI digunakan semasa mengetatkan bolt?")
    q3 = st.radio(
        "Pilih teknik yang betul:",
        ("Pusingan Jam (Clockwise)", 
         "Star / Cross Pattern (Silang)", 
         "Pusingan Lawan Jam (Counter-Clockwise)"),
        key="q3"
    )

    # --- SOALAN 4: TORQUE STAGES (Berdasarkan PDF Page 19/24) ---
    st.subheader("4. Peringkat Tork (Torque Stages)")
    st.write("Berapakah peratusan tork yang betul untuk 3 pusingan pertama?")
    q4 = st.radio(
        "Turutan peratusan:",
        ("50% -> 75% -> 100%", 
         "30% -> 60% -> 100%", 
         "10% -> 50% -> 100%"),
        key="q4"
    )

    # Butang Hantar
    submitted = st.form_submit_button("Hantar Jawapan")

# --- LOGIK PEMARKAHAN ---
if submitted:
    score = 0
    
    # Semak Soalan 1 [Cite: 384]
    if q1 == "Untuk mengalirkan sisa cecair ke bawah & elak terkena badan (Line of Fire)":
        score += 1
    else:
        st.error("Soalan 1 Salah: Rujuk 'Line of Fire' safety.")

    # Semak Soalan 2 [Cite: 361]
    if q2 == "🟡 Kuning (Flange Tightened - Torqued)":
        score += 1
    else:
        st.error("Soalan 2 Salah: Kuning adalah untuk Flange Tightened.")

    # Semak Soalan 3 [Cite: 267]
    if q3 == "Star / Cross Pattern (Silang)":
        score += 1
    else:
        st.error("Soalan 3 Salah: Mesti guna Cross Pattern untuk elak kebocoran.")

    # Semak Soalan 4 [Cite: 310]
    if q4 == "30% -> 60% -> 100%":
        score += 1
    else:
        st.error("Soalan 4 Salah: Ikut ASME PCC-1 (30, 60, 100).")

    # KEPUTUSAN AKHIR
    st.markdown("---")
    if score == 4:
        st.balloons()
        st.success(f"TAHNIAH! Markah Penuh: {score}/4")
        st.info("✅ Kod Akses VR Anda: **8829**")
        st.write("Sila masukkan kod ini dalam Meta Quest 3 untuk memulakan simulasi.")
    elif score >= 2:
        st.warning(f"Markah Anda: {score}/4. Sila rujuk semula modul AR.")
    else:
        st.error(f"Markah Anda: {score}/4. Anda gagal ujian kompetensi.")
