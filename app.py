import streamlit as st
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="NJ Family Court", page_icon="⚖️", layout="centered")

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .ticket { border: 2px solid #333; padding: 20px; background-color: #fcfbf9; font-family: 'Courier New', monospace; }
    .header { text-align: center; border-bottom: 2px solid #333; margin-bottom: 10px; font-weight: bold; }
    .statute { color: #b30000; font-weight: bold; }
    .stButton>button { width: 100%; background-color: #b30000; color: white; }
</style>
""", unsafe_allow_html=True)

st.title("🚓 Family Citation Writer")
st.caption("Official Title 39-H Issuance System")

# --- INPUT SECTION (No Form) ---
# 1. DEFENDANT
defendant = st.text_input("Defendant Name:", placeholder="Enter name (e.g. Ayden, Mom...)")

# 2. LOCATION
location = st.text_input("Location of Incident:", placeholder="Living Room, Kitchen...")

st.divider()

# 3. VIOLATION (Live Toggle)
violation_mode = st.radio("Violation Type:", ["Select from List", "Write Custom"], horizontal=True)

if violation_mode == "Select from List":
    violation_text = st.selectbox("Select Violation:", [
        "39:H-10 :: Empty Water Pitcher",
        "39:H-22 :: Lights Left On",
        "39:H-45 :: Thermostat Tampering",
        "39:H-50 :: Dishwasher Loading Error",
        "39:H-99 :: Gaming Past Curfew"
    ])
else:
    violation_text = st.text_input("Enter Custom Violation:", placeholder="e.g. Ate the last slice of pizza")

st.divider()

# 4. PENALTY (Live Toggle)
penalty_mode = st.radio("Penalty Type:", ["Select from List", "Write Custom"], horizontal=True)

if penalty_mode == "Select from List":
    penalty_text = st.selectbox("Select Penalty:", ["Verbal Warning", "Trash Duty", "Mow Lawn", "Loss of WiFi (24h)", "Dish Duty"])
else:
    penalty_text = st.text_input("Enter Custom Penalty:", placeholder="e.g. Buy Dad a coffee")

st.divider()

# --- ISSUE BUTTON ---
if st.button("🚨 ISSUE CITATION"):
    if not defendant:
        st.error("⚠️ You must enter a Defendant name!")
    else:
        # The Ticket HTML
        html_ticket = f"""
        <div class="ticket">
            <div class="header">
                STATE OF NEW JERSEY<br>
                FAMILY MUNICIPAL COURT<br>
                SUMMONS # {datetime.datetime.now().strftime('%m%d-%H%M')}
            </div>
            <p><b>DATE:</b> {datetime.date.today()}</p>
            <p><b>DEFENDANT:</b> {defendant.upper()}</p>
            <p><b>LOCATION:</b> {location.upper()}</p>
            <hr>
            <p><b>VIOLATION:</b> <span class="statute">{violation_text}</span></p>
            <hr>
            <p><b>PENALTY ASSESSED:</b></p>
            <p><b>{penalty_text.upper()}</b></p>
            <hr>
            <p style="text-align:center; margin-top:20px;"><i>ISSUING OFFICER: DAD</i></p>
        </div>
        """
        st.markdown(html_ticket, unsafe_allow_html=True)
