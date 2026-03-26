import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Birthday Surprise 🎂", layout="wide")

# ================= STATE =================
if "started" not in st.session_state:
    st.session_state.started = False

# ================= BUTTON =================
if not st.session_state.started:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)

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

    /* FLOATING */
    .floating {{
        position: absolute;
        bottom: -50px;
        font-size: 30px;
        animation: floatUp linear infinite;
    }}

    @keyframes floatUp {{
        0% {{ transform: translateY(0); opacity:1; }}
        100% {{ transform: translateY(-110vh); opacity:0; }}
    }}

    /* CAKE */
    .cake {{
        position: absolute;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 200px;
        height: 120px;
        background: pink;
        border-radius: 50% 50% 40% 40%;
        text-align: center;
        font-size: 40px;
        padding-top: 30px;
        animation: cakeIn 1s ease;
    }}

    @keyframes cakeIn {{
        from {{ transform: translate(-50%, -60%) scale(0.5); opacity:0; }}
        to {{ transform: translate(-50%, -50%) scale(1); opacity:1; }}
    }}

    /* CANDLE */
    .candle {{
        position: absolute;
        top: -20px;
        font-size: 20px;
        animation: flame 1s infinite alternate;
    }}

    @keyframes flame {{
        from {{ opacity:1; }}
        to {{ opacity:0.5; }}
    }}

    /* CONFETTI EXPLOSION */
    .confetti {{
        position: absolute;
        width: 6px;
        height: 6px;
        background: black;
        top: 50%;
        left: 50%;
        animation: explode 1s ease forwards;
    }}

    @keyframes explode {{
        0% {{ transform: translate(0,0); opacity:1; }}
        100% {{ transform: translate(var(--x), var(--y)); opacity:0; }}
    }}

    /* TEXT */
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
        animation-delay: 4s;
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

        <!-- CAKE -->
        <div id="cake" class="cake">
            19
            <div id="flame" class="candle">🔥</div>
        </div>

        <!-- TEXT -->
        <div class="text">🎉 Happy Birthday Rifki 💖</div>

    </div>

    <script>
    setTimeout(() => {{
        // matiin api
        document.getElementById("flame").innerHTML = "💨";
    }}, 2000);

    setTimeout(() => {{
        // hilangin cake
        document.getElementById("cake").style.display = "none";

        // ledakan confetti
        for (let i = 0; i < 80; i++) {{
            let c = document.createElement("div");
            c.className = "confetti";
            c.style.setProperty('--x', (Math.random()*400-200)+'px');
            c.style.setProperty('--y', (Math.random()*400-200)+'px');
            document.body.appendChild(c);
        }}
    }}, 3000);
    </script>

    </body>
    </html>
    """

    components.html(html_code, height=700)
