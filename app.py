import streamlit as st
import datetime

# --- 1. CONFIGURATION (MUST BE FIRST) ---
st.set_page_config(page_title="Dad Command Center", page_icon="👔", layout="centered")

# --- 2. SIDEBAR MENU ---
with st.sidebar:
    st.title("👔 DadOS v1.0")
    st.write("Select Tool:")
    app_mode = st.radio("", ["🚓 Citation Writer", "🚜 Lawn Enforcer"])
    st.divider()
    st.caption("System Status: OPERATIONAL")

# --- 3. APP: CITATION WRITER ---
if app_mode == "🚓 Citation Writer":
    # Custom CSS for the ticket
    st.markdown("""
    <style>
        .ticket { border: 2px solid black; padding: 20px; background-color: #fcfbf9; font-family: monospace; }
        .statute { color: #b30000; font-weight: bold; }
        div[data-testid="stForm"] { border: 2px solid #ddd; padding: 20px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

    st.title("🚓 Family Citation Book")
    st.markdown("### Official Title 39-H Issuance System")

    with st.form("ticket_form"):
        c1, c2 = st.columns(2)
        defendant = c1.selectbox("Defendant:", ["Ayden", "Mom", "Brother", "The Dog"])
        location = c2.text_input("Location:", placeholder="Living Room, Kitchen...")
        
        violation = st.selectbox("Violation (Title 39-H):", [
            "39:H-10 :: Empty Water Pitcher",
            "39:H-22 :: Lights Left On in Empty Room",
            "39:H-45 :: Thermostat Tampering",
            "39:H-50 :: Failure to Rinse Dish",
            "39:H-88 :: Shoes Left in Hallway",
            "39:H-99 :: Gaming Past Curfew"
        ])
        
        penalty = st.selectbox("Penalty Assessed:", ["Verbal Warning", "Trash Duty", "Mow Lawn", "Loss of WiFi (24h)", "Dish Duty"])
        
        submitted = st.form_submit_button("🚨 ISSUE TICKET")

    if submitted:
        st.divider()
        html_ticket = f"""
        <div class="ticket">
            <h3 style="text-align:center; border-bottom:2px solid black; margin-bottom:10px;">NJ FAMILY COURT</h3>
            <p><b>DATE:</b> {datetime.date.today()}</p>
            <p><b>DEFENDANT:</b> {defendant.upper()}</p>
            <p><b>LOCATION:</b> {location.upper()}</p>
            <hr>
            <p><b>VIOLATION:</b> <span class="statute">{violation}</span></p>
            <hr>
            <p><b>PENALTY:</b> {penalty.upper()}</p>
            <p style="text-align:center; font-size:10px; margin-top:20px;">ISSUING OFFICER: DAD</p>
        </div>
        """
        st.markdown(html_ticket, unsafe_allow_html=True)

# --- 4. APP: LAWN ENFORCER ---
elif app_mode == "🚜 Lawn Enforcer":
    st.title("🚜 The Lawn Enforcer")
    st.markdown("### Operational Readiness Dashboard")
    st.info("Calibrate current sector conditions:")

    col1, col2 = st.columns(2)
    with col1:
        temp = st.slider("🌡️ Temperature (°F)", 40, 105, 75)
        wind = st.slider("🌬️ Wind Speed (MPH)", 0, 40, 5)

    with col2:
        grass = st.radio("💧 Grass Status:", ["Bone Dry", "Morning Dew", "Wet / Rained Recently"])
        
    # LOGIC
    status = "GO"
    reasons = []

    if temp > 88:
        status = "NO GO"
        reasons.append("⛔ HEAT: Too hot for operator safety.")
    elif temp < 55:
        status = "CAUTION"
        reasons.append("⚠️ COLD: Grass may tear.")

    if grass == "Wet / Rained Recently":
        status = "NO GO"
        reasons.append("⛔ MOISTURE: Deck clogging risk.")
    elif grass == "Morning Dew":
        status = "CAUTION"
        reasons.append("⚠️ DEW: Wait 60 minutes for drying.")

    if wind > 20:
        status = "NO GO"
        reasons.append("⛔ WIND: Debris blowback risk.")

    st.divider()
    if status == "GO":
        st.success("## 🟢 GREEN LIGHT: PROCEED")
        st.markdown("**Conditions are optimal. Deploy equipment.**")
        if st.button("🚜 Launch Mowing Sequence"):
            st.balloons()
    elif status == "CAUTION":
        st.warning("## 🟡 YELLOW LIGHT: PROCEED WITH CAUTION")
        for r in reasons: st.write(r)
    else:
        st.error("## 🔴 RED LIGHT: STAND DOWN")
        st.markdown("**Mission Aborted. Return to Base.**")
        for r in reasons: st.write(r)
