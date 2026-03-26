import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Birthday Surprise 🎂", layout="wide")

# ================= STATE =================
if "started" not in st.session_state:
    st.session_state.started = False

# ================= CENTER BUTTON =================
if not st.session_state.started:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)  # spacer biar ke tengah

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎁 Click Here"):
            st.session_state.started = True
            st.rerun()

# ================= ANIMATION =================
if st.session_state.started:
    emojis = ["🎂","🎉","💛","🍫","✨","💖"]

    elements = ""

    for i in range(60):
        left = random.randint(0, 100)
        duration = random.randint(5, 12)
        delay = random.randint(0, 5)
        emoji = random.choice(emojis)

        elements += f"""
        <div class="floating" style="
            left:{left}%;
            animation-duration:{duration}s;
            animation-delay:{delay}s;">
            {emoji}
        </div>
        """

    for i in range(80):
        left = random.randint(0, 100)
        duration = random.randint(4, 10)
        delay = random.randint(0, 5)

        elements += f"""
        <div class="confetti" style="
            left:{left}%;
            animation-duration:{duration}s;
            animation-delay:{delay}s;">
        </div>
        """

    html_code = f"""
    <html>
    <head>
    <style>
    body {{
        margin: 0;
        overflow: hidden;
        background: white;
    }}

    .container {{
        position: relative;
        width: 100%;
        height: 100vh;
    }}

    .floating {{
        position: absolute;
        bottom: -50px;
        font-size: 30px;
        animation: floatUp linear infinite;
    }}

    .confetti {{
        position: absolute;
        width: 6px;
        height: 6px;
        background: black;
        bottom: -10px;
        animation: confettiFall linear infinite;
    }}

    @keyframes floatUp {{
        0% {{ transform: translateY(0); opacity:1; }}
        100% {{ transform: translateY(-110vh); opacity:0; }}
    }}

    @keyframes confettiFall {{
        0% {{ transform: translateY(0) rotate(0deg); }}
        100% {{ transform: translateY(-110vh) rotate(720deg); }}
    }}

    .text {{
        position: absolute;
        top: 40%;
        width: 100%;
        text-align: center;
        font-size: 50px;
        color: black;
        font-weight: bold;
        opacity: 0;
        animation: fadeIn 2s ease forwards;
        animation-delay: 1s;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(20px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}
    </style>
    </head>

    <body>
        <div class="container">
            {elements}
            <div class="text">🎉 Happy Birthday Rifki 💖</div>
        </div>
    </body>
    </html>
    """

    components.html(html_code, height=700)
