import streamlit as st
import random
import streamlit.components.v1 as components

st.set_page_config(page_title="Birthday Surprise 🎂", layout="wide")

# STATE
if "started" not in st.session_state:
    st.session_state.started = False

# BUTTON
if not st.session_state.started:
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎁 Click Here"):
            st.session_state.started = True
            st.rerun()

# ANIMATION
if st.session_state.started:

    emojis = ["🎂","🎉","💛","🍫","✨","💖"]

    floating = ""
    for i in range(60):
        left = random.randint(0, 100)
        duration = random.randint(5, 12)
        delay = random.randint(0, 5)
        emoji = random.choice(emojis)

        floating += f"""
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
        margin:0;
        overflow:hidden;
        background:white;
    }}

    .container {{
        position:relative;
        width:100%;
        height:100vh;
    }}

    /* 🎂 CAKE POP OUT */
    .cake {{
        position:absolute;
        top:50%;
        left:50%;
        transform:translate(-50%, -50%) scale(0.3);
        width:240px;
        height:150px;
        animation:popOut 1.5s ease forwards;
    }}

    @keyframes popOut {{
        0% {{ transform:translate(-50%, -50%) scale(0.3); opacity:0; }}
        60% {{ transform:translate(-50%, -50%) scale(1.2); }}
        100% {{ transform:translate(-50%, -50%) scale(1); opacity:1; }}
    }}

    .layer-bottom {{
        width:240px;
        height:80px;
        background:#f6d56b;
        border-radius:20px;
        position:absolute;
        bottom:0;
    }}

    .layer-middle {{
        width:240px;
        height:20px;
        background:#d98cb3;
        position:absolute;
        bottom:60px;
        border-radius:10px;
    }}

    .layer-top {{
        width:240px;
        height:40px;
        background:#f7a8c5;
        border-radius:20px 20px 10px 10px;
        position:absolute;
        top:0;
    }}

    .plate {{
        width:280px;
        height:20px;
        background:#c7e6f5;
        border-radius:50%;
        position:absolute;
        bottom:-15px;
        left:-20px;
    }}

    /* 🔢 NUMBER */
    .number {{
        position:absolute;
        top:-50px;
        font-size:40px;
        font-weight:bold;
    }}

    .one {{ left:70px; }}
    .nine {{ left:130px; }}

    /* 🔥 FLAME */
    .flame {{
        position:absolute;
        top:-30px;
        left:5px;
        font-size:26px;
        animation:flicker 0.4s infinite alternate;
    }}

    @keyframes flicker {{
        from {{ transform:scale(1); }}
        to {{ transform:scale(1.3); }}
    }}

    /* 💥 CONFETTI */
    .confetti {{
        position:absolute;
        width:6px;
        height:6px;
        background:black;
        top:50%;
        left:50%;
        animation: explode 1s ease forwards;
    }}

    @keyframes explode {{
        0% {{ transform:translate(0,0); opacity:1; }}
        100% {{ transform:translate(var(--x), var(--y)); opacity:0; }}
    }}

    /* 🎈 FLOATING (MUNCUL BELAKANGAN) */
    .floating {{
        position:absolute;
        bottom:-50px;
        font-size:28px;
        animation: floatUp linear infinite;
        opacity:0;
    }}

    .show-bg .floating {{
        opacity:1;
    }}

    @keyframes floatUp {{
        0% {{ transform:translateY(0); opacity:1; }}
        100% {{ transform:translateY(-110vh); opacity:0; }}
    }}

    /* 🎉 TEXT */
    .text {{
        position:absolute;
        top:40%;
        width:100%;
        text-align:center;
        font-size:50px;
        color:black;
        font-weight:bold;
        opacity:0;
    }}

    .show-bg .text {{
        animation:fadeIn 2s ease forwards;
    }}

    @keyframes fadeIn {{
        from {{ opacity:0; transform:translateY(20px); }}
        to {{ opacity:1; transform:translateY(0); }}
    }}

    </style>
    </head>

    <body>

    <div id="main" class="container">

        {floating}

        <!-- CAKE -->
        <div id="cake" class="cake">
            <div class="layer-top"></div>
            <div class="layer-middle"></div>
            <div class="layer-bottom"></div>
            <div class="plate"></div>

            <div class="number one">1<div class="flame">🔥</div></div>
            <div class="number nine">9<div class="flame">🔥</div></div>
        </div>

        <!-- TEXT -->
        <div class="text">🎉 Happy Birthday Rifki 💖</div>

    </div>

    <script>

    // 💨 tiup
    setTimeout(() => {{
        document.querySelectorAll(".flame").forEach(f => f.innerHTML = "💨");
    }}, 2000);

    // 💥 explode + munculin bg + teks
    setTimeout(() => {{
        document.getElementById("cake").style.display = "none";

        for (let i = 0; i < 100; i++) {{
            let c = document.createElement("div");
            c.className = "confetti";
            c.style.setProperty('--x', (Math.random()*500-250)+'px');
            c.style.setProperty('--y', (Math.random()*500-250)+'px');
            document.body.appendChild(c);
        }}

        // aktifin background + text
        document.getElementById("main").classList.add("show-bg");

    }}, 3000);

    </script>

    </body>
    </html>
    """

    components.html(html_code, height=700)
