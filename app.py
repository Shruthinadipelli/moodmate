import streamlit as st
from emotion_detect import detect_emotion
from text_emotion import detect_text_emotion
from recommender import recommend_music
from youtube_recommender import open_youtube

# Page config
st.set_page_config(page_title="MoodMate", layout="centered")

# Title
st.markdown("<h1 style='text-align: center;'>🎵 MoodMate</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Emotion-Based Music Recommendation System</h4>", unsafe_allow_html=True)

st.write("---")

# Mode selection
option = st.radio("Choose Input Type:", ["Text Emotion (NLP)", "Webcam Emotion"])

# =========================
# TEXT MODE
# =========================
if option == "Text Emotion (NLP)":
    st.subheader("💬 Describe Your Feeling")

    user_text = st.text_input("Enter how you feel (e.g., I am feeling sad today)")

    if st.button("🎯 Recommend Songs"):
        if user_text:
            emotion = detect_text_emotion(user_text)
            st.success(f"Detected Emotion: {emotion}")

            songs = recommend_music(emotion)

            st.write("### 🎶 Recommended Songs")

            for song in songs:
                st.markdown(f"""
                <div style="padding:10px; border-radius:10px; border:1px solid #ccc; margin-bottom:10px;">
                    <b>🎵 {song['song']}</b><br>
                    👤 {song['artist']}<br>
                </div>
                """, unsafe_allow_html=True)

                if st.button(f"▶️ Play {song['song']}"):
                   open_youtube(song['song'], song['artist'])

        else:
            st.warning("Please enter how you feel!")

# =========================
# WEBCAM MODE
# =========================
elif option == "Webcam Emotion":
    st.subheader("📷 Detect Emotion from Webcam")

    if st.button("🎥 Start Detection"):
        st.info("Press 'q' to stop webcam")

        emotion = detect_emotion()

        st.success(f"Detected Emotion: {emotion}")

        songs = recommend_music(emotion)

        st.write("### 🎶 Recommended Songs")

        for song in songs:
            st.markdown(f"""
            <div style="padding:10px; border-radius:10px; border:1px solid #ccc; margin-bottom:10px;">
                <b>🎵 {song['song']}</b><br>
                👤 {song['artist']}<br>
            </div>
            """, unsafe_allow_html=True)

            st.link_button("▶️ Play on YouTube", song['link'])
