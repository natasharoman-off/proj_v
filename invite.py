import streamlit as st

# Set page configuration
st.set_page_config(page_title="Valentine's Quiz & Proposal 💖", layout="centered")

# Initialize session state
if "quiz_completed" not in st.session_state:
    st.session_state.quiz_completed = False
    st.session_state.quiz_score = 0

# File paths (Update with actual video file paths)
yes_video = "happy.mp4"  # Video for passing the quiz
no_video = "sad.mp4"  # Video for failing the quiz

# Quiz Section
if not st.session_state.quiz_completed:
    st.markdown("<h1 style='text-align: center; color: #FF4081;'>💖 Valentine's Quiz 💖</h1>", unsafe_allow_html=True)
    st.write("Answer these fun questions to proceed!")

    # Custom Quiz Questions
    q1 = st.radio("1️⃣ yaaru peru paacha and poocha", 
                                   ["a) hotbag and catkeychain", "b) cat keychain and hotbag", "c) Therla cause im bad"], index=None, key="q1")

    q2 = st.radio("2️⃣ what was the first nickname i gave to u?", 
                                   ["a) water car", "b) robot car🧸", "c) poochi car 🌸"], index=None, key="q2")

    q3 = st.radio("3️⃣ Why do u think i like u?", 
                                   ["a) u look so ahhhhhhh skibidiiiiiiiiiiiiiii😻", "b) cause ur gay🐆", "c) because u like kids🐱"], index=None, key="q3")

    # Submit button
    if st.button("Submit Answers 💌"):
        score = 0
        # Check if answers are selected before scoring
        if q1 and q2 and q3:
            if q1 == "b":  # Purring softly shows love
                score += 1
            if q2 == "b":  # Cat plushie is a great gift
                score += 1
            if q3 == "a":  # Ragdoll cats are affectionate
                score += 1
            
            # Save score and mark quiz as completed
            st.session_state.quiz_score = score
            st.session_state.quiz_completed = True
        else:
            st.warning("Please answer all questions before submitting!")

# After Quiz - Show Results with Custom Messages
if st.session_state.quiz_completed:
    st.markdown("<h1 style='text-align: center; color: #FF4081;'>💌 THANK YOU FOR EVERYTHING CHELLA KUTTI💕</h1>", unsafe_allow_html=True)

    if st.session_state.quiz_score >= 2:
        st.success("You are the best carrrrrrrr! 🎉🐱")
        st.balloons()  # Confetti effect 🎉
        st.video(yes_video)
    else:
        st.warning("KUTTI CHELLA PAACHA CAR LOVE U SO MUCHHHHHHHH! 😆💖")
        st.video(no_video)