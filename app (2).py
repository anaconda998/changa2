import streamlit as st
import streamlit.components.v1 as components
import time

# ------------------------------
# UI Setup: Background Image
# ------------------------------
def set_background_from_url(image_url: str):
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        html, body, [class*="css"] {{
            font-family: 'Georgia', serif;
            color: #000000 !important;
        }}
        .fade-in {{
            opacity: 0;
            animation: fadeIn 2s ease forwards;
        }}
        @keyframes fadeIn {{
            to {{
                opacity: 1;
            }}
        }}
        </style>
    """, unsafe_allow_html=True)

set_background_from_url("https://raw.githubusercontent.com/priyanshugarg29/Data/main/bgimage.gif")

# ------------------------------
# Session Flags
# ------------------------------
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

if "began_journey" not in st.session_state:
    st.session_state.began_journey = False

if "countdown_done" not in st.session_state:
    st.session_state.countdown_done = False

# ------------------------------
# 1. Begin Journey Button
# ------------------------------
if not st.session_state.began_journey:
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.markdown("## A quiet moment before we begin...")
    if st.button("✨ Begin Journey", use_container_width=True):
        st.session_state.began_journey = True
        st.rerun()
    st.stop()

# ------------------------------
# 2. Music with Mute/Unmute
# ------------------------------
components.html("""
    <div style="position: fixed; bottom: 20px; left: 20px; z-index: 9999;">
        <audio id="bg-music" autoplay loop>
            <source src="https://raw.githubusercontent.com/priyanshugarg29/Data/main/SolasLogin.mp3" type="audio/mpeg">
        </audio>
        <button onclick="toggleMute()" id="mute-btn"
            style="padding: 6px 14px; font-size: 14px; border-radius: 6px;
                   background-color: #ffffffaa; color: #000; border: none;
                   box-shadow: 1px 1px 3px rgba(0,0,0,0.2);">
            🔊 Mute
        </button>
        <script>
            const music = document.getElementById('bg-music');
            const btn = document.getElementById('mute-btn');
            music.volume = 0.5;
            function toggleMute() {
                music.muted = !music.muted;
                btn.innerText = music.muted ? '🔇 Unmute' : '🔊 Mute';
            }
        </script>
    </div>
""", height=120)

# ------------------------------
# 3. Password Authentication
# ------------------------------
if not st.session_state.authenticated:
    st.title("Welcome to the Journey...")
    st.caption("A whisper only you will know")

    try:
        correct_password = st.secrets["auth"]["passcode"]
    except KeyError:
        st.error("Missing passcode in Streamlit secrets.")
        st.stop()

    password = st.text_input("Enter the shared code to begin:", type="password")

    if password:
        if password == correct_password:
            st.session_state.authenticated = True
            st.success("Access granted. Welcome.")
            st.rerun()
        else:
            st.error("That doesn’t seem right. Try again.")

    st.stop()

# ------------------------------
# 4. Post-Login Message & Countdown
# ------------------------------
if not st.session_state.countdown_done:
    st.markdown("### Hello Diksha, you’ve unlocked the first step of the journey.")
    st.caption("Let’s begin walking through memory — one quiet whisper at a time.")

    with st.empty():
        for i in range(8, 0, -1):
            st.markdown(f"⏳ Redirecting in **{i}** seconds...")
            time.sleep(1)

    # Pause with just background and music
    st.empty()  # Clear screen
    time.sleep(2)

    st.session_state.countdown_done = True
    st.rerun()

# ------------------------------
# 5. Poetic Paragraphs (Timed)
# ------------------------------
poem_parts = [
    "It started with visiting WBS for collecting BRP documents...",
    "and free pizza — but you didn't want any, and I didn’t know what I wanted either.",
    "We crossed paths at the city center, always stood around but not really close — and yet, the moment waited for our friendship.",
    "I let you down once — not knowingly, just unaware.",
    "But even then, my soul must have known... this was a connection it wouldn’t let pass.",
    "The shell I picked at Cardiff — I still carry it. Not just as a souvenir anymore, but a silent vow...that -",
    "I’ll remember you… even if we never meet again.",
    "Somewhere between disturbing you and listening to you,",
    "a friendship bloomed — no name, just truth.",
    "You made me feel safe… like home never left me, it just waited in your eyes.",
    "I never rushed to name this feeling.",
    "Because fleeting things chase labels — but real ones grow silently.",
    "Now you’re leaving. And something inside me has quietly shifted… like I am not just saying goodbye to a good friend, but to a possible future.",
    "Even now, I honestly don’t seek answers — just one last promise:",
    "That you live the life your heart dreams of.",
    "And.......",
    "if our stars ever realign — I’ll pick up from where we never left off."
]

st.empty()  # Clear screen

for line in poem_parts:
    with st.container():
        st.markdown(f"<div class='fade-in'><h4 style='text-align: center;'>{line}</h4></div>", unsafe_allow_html=True)
        time.sleep(4)

# ------------------------------
# 6. Closing Note
# ------------------------------
closing = """
<div class='fade-in'>
<h4 style='text-align: center; margin-top: 60px;'>
Some friendships don’t fade, they just find a quieter place to live — <br>
like a soft light I’ll always carry in me, <br>
wherever I go...
</h4>
</div>
"""
st.markdown(closing, unsafe_allow_html=True)
time.sleep(6)

# ------------------------------
# 7. Final Line
# ------------------------------
final = """
<div class='fade-in'>
<h5 style='text-align: center; margin-top: 40px;'>
Abhi tak toh sach batau toh bahana tha —<br>
but abb yaar sach mein bore toh bahoot hunga :D
</h5>
</div>
"""
st.markdown(final, unsafe_allow_html=True)
