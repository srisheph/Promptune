
import streamlit as st
from utils import authenticate_user, register_user, get_recommended_songs
import time
import re  # For extracting video ID from URL

st.set_page_config(page_title="Promptune 🎶", layout="wide")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
        body { font-family: 'Poppins', sans-serif; background-color: #121212; color: white; }
        .navbar { background-color: #1DB954; padding: 15px; display: flex; justify-content: space-between; border-radius: 8px; }
        .navbar-title { font-size: 22px; font-weight: bold; color: black; }
        .navbar-user { font-size: 18px; font-weight: bold; }
        .song-card { display: flex; align-items: center; padding: 15px; border-radius: 10px; margin: 10px 0; background-color: #282828; }
        .song-card img { width: 150px; height: auto; border-radius: 8px; margin-right: 15px; }
        .song-info { flex: 1; }
        .song-title { font-size: 18px; font-weight: bold; color: #1DB954; margin: 5px 0; }
        .song-artist { font-size: 14px; color: #BBBBBB; margin-bottom: 8px; }
        .listen-button { background: linear-gradient(135deg, #1DB954, #19a74b); color: white; padding: 6px 12px; border-radius: 6px; font-size: 14px; text-decoration: none; }
        .listen-button:hover { background: linear-gradient(135deg, #19a74b, #1DB954); }
    </style>
""", unsafe_allow_html=True)

# Extract YouTube Thumbnail Function
def get_youtube_thumbnail(video_url):
    match = re.search(r"v=([\w-]+)", video_url)  # Extract video ID
    if match:
        return f"https://img.youtube.com/vi/{match.group(1)}/0.jpg"
    return "https://via.placeholder.com/150x150?text=No+Cover"

# NAVIGATION
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    username = st.session_state.username
    st.markdown(f"""
        <div class="navbar">
            <div class="navbar-title">🎶 Promptune</div>
            <div class="navbar-user">Welcome, {username} </div>
        </div>
    """, unsafe_allow_html=True)

    # Music Recommendation Section
    st.title("🎵 Discover Your Next Favorite Song")
    prompt = st.text_input("Describe your mood or vibe:")

    if st.button("🎧 Get Recommendations"):
        if prompt.strip():
            with st.spinner("Fetching your recommendations..."):
                progress_bar = st.progress(0)
                for i in range(100):
                    time.sleep(0.01)
                    progress_bar.progress(i + 1)

                songs = get_recommended_songs(prompt)
                if songs:
                    for song in songs:
                        cover_image = get_youtube_thumbnail(song["url"])  # Get cover image
                        st.markdown(f"""
                            <div class="song-card">
                                <img src="{cover_image}" alt="Cover Image">
                                <div class="song-info">
                                    <p class="song-title">{song['title']}</p>
                                    <p class="song-artist">Artist: {song['artist']}</p>
                                    <a class="listen-button" href="{song['url']}" target="_blank">Listen on YouTube</a>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("No songs found! Try another prompt.")
        else:
            st.error("Please enter a prompt!")

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.rerun()

else:
    # LOGIN & REGISTER PAGE
    st.markdown("""
        <div style="background: linear-gradient(135deg, #1DB954, #121212); padding: 40px; border-radius: 10px; text-align: center;">
            <h1 style="color: white; font-size: 48px; font-weight: bold;">🎶 Promptune</h1>
            <p style="color: white; font-size: 20px;">Your personal DJ for every mood.</p>
        </div>
    """, unsafe_allow_html=True)

    page = st.radio("Choose an option:", ["Login", "Register"])

    if page == "Login":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if username.strip() and password.strip():
                if authenticate_user(username, password):
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success(f"Welcome, {username}!")
                    st.rerun()
                else:
                    st.error("Invalid username or password.")
            else:
                st.error("Username and password cannot be empty!")

    elif page == "Register":
        new_username = st.text_input("Choose a Username")
        new_password = st.text_input("Create a Password", type="password")
        name = st.text_input("Your Name")

        if st.button("Register"):
            if new_username.strip() and new_password.strip() and name.strip():
                response = register_user(new_username, new_password, name)
                st.success(response)
            else:
                st.error("All fields are required!")

