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

    html_code = """
    <html>
    <head>
    <style>
    body {
        margin:0;
        overflow:hidden;
        background:white;
    }

    .container {
        position:relative;
        width:100%;
        height:100vh;
    }

    /* 🎂 CAKE (lebih realistis) */
    .cake {
        position:absolute;
        top:50%;
        left:50%;
        transform:translate(-50%, -50%);
        width:220px;
        height:140px;
    }

    .layer-bottom {
        width:220px;
        height:80px;
        background:#f6d56b;
        border-radius:20px;
        position:absolute;
        bottom:0;
    }

    .layer-middle {
        width:220px;
        height:20px;
        background:#d98cb3;
        position:absolute;
        bottom:60px;
        border-radius:10px;
    }

    .layer-top {
        width:220px;
        height:40px;
        background:#f7a8c5;
        border-radius:20px 20px 10px 10px;
        position:absolute;
        top:0;
    }

    .plate {
        width:260px;
        height:20px;
        background:#c7e6f5;
        border-radius:50%;
        position:absolute;
        bottom:-15px;
        left:-20px;
    }

    /* lilin */
    .candle {
        position:absolute;
        width:6px;
        height:30px;
        background:red;
        top:-30px;
    }

    .flame {
        position:absolute;
        top:-15px;
        left:-3px;
        font-size:14px;
        animation: flicker 0.5s infinite alternate;
    }

    @keyframes flicker {
        from {opacity:1;}
        to {opacity:0.5;}
    }

    /* TEXT */
    .text {
        position:absolute;
        top:40%;
        width:100%;
        text-align:center;
        font-size:50px;
        color:black;
        font-weight:bold;
        opacity:0;
        animation:fadeIn 2s ease forwards;
        animation-delay:4s;
    }

    @keyframes fadeIn {
        from {opacity:0; transform:translateY(20px);}
        to {opacity:1; transform:translateY(0);}
    }

    /* CONFETTI */
    .confetti {
        position:absolute;
        width:6px;
        height:6px;
        background:black;
        top:50%;
        left:50%;
        animation: explode 1s ease forwards;
    }

    @keyframes explode {
        0% {transform:translate(0,0); opacity:1;}
        100% {transform:translate(var(--x), var(--y)); opacity:0;}
    }

    </style>
    </head>

    <body>

    <div class="container">

        <!-- CAKE -->
        <div id="cake" class="cake">
            <div class="layer-top"></div>
            <div class="layer-middle"></div>
            <div class="layer-bottom"></div>
            <div class="plate"></div>

            <!-- lilin random posisi -->
            <div class="candle" style="left:30px;"><div class="flame">🔥</div></div>
            <div class="candle" style="left:60px; background:orange;"><div class="flame">🔥</div></div>
            <div class="candle" style="left:90px; background:blue;"><div class="flame">🔥</div></div>
            <div class="candle" style="left:120px; background:green;"><div class="flame">🔥</div></div>
            <div class="candle" style="left:150px; background:yellow;"><div class="flame">🔥</div></div>
            <div class="candle" style="left:180px;"><div class="flame">🔥</div></div>
        </div>

        <!-- TEXT -->
        <div class="text">🎉 Happy Birthday Rifki 💖</div>

    </div>

    <script>

    // 🔥 padam
    setTimeout(() => {
        document.querySelectorAll(".flame").forEach(f => f.innerHTML = "💨");
    }, 2000);

    // 💥 explode + hide cake
    setTimeout(() => {
        document.getElementById("cake").style.display = "none";

        for (let i = 0; i < 100; i++) {
            let c = document.createElement("div");
            c.className = "confetti";
            c.style.setProperty('--x', (Math.random()*500-250)+'px');
            c.style.setProperty('--y', (Math.random()*500-250)+'px');
            document.body.appendChild(c);
        }
    }, 3000);

    </script>

    </body>
    </html>
    """

    components.html(html_code, height=700)
