
import streamlit as st

# ----------------------------------
# 1. PAGE CONFIGURATION
# ----------------------------------

st.set_page_config(
    page_title="EduBridge AI",
    page_icon="📚",
    layout="wide"
)

# ----------------------------------
# 2. SESSION STATE
# ----------------------------------

if "tasks" not in st.session_state:
    st.session_state.tasks = []

# ----------------------------------
# 3. APPLICATION HEADER
# ----------------------------------

st.title("📚 EduBridge AI")

st.subheader("Your Smart Learning Assistant")

st.write(
    "Learn Better. Prepare Smarter. "
    "Succeed Together."
)

st.divider()

# ----------------------------------
# 4. SIDEBAR NAVIGATION
# ----------------------------------

st.sidebar.title("EduBridge AI")

menu = st.sidebar.radio(
    "Navigate",
    [
        "Home",
        "Homework Assistant",
        "Exam Preparation",
        "Multilingual Learning",
        "Study Planner"
    ]
)

# ----------------------------------
# 5. HOME PAGE
# ----------------------------------

if menu == "Home":

    st.header("Welcome to EduBridge AI 👋")

    st.write(
        "Your personal learning platform "
        "powered by Artificial Intelligence."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("📖 Homework Assistance")
        st.info("📝 Examination Preparation")

    with col2:
        st.info("🌍 Multilingual Learning")
        st.info("📅 Personal Study Planner")

    st.success(
        "Start your learning journey today!"
    )

# ----------------------------------
# 6. HOMEWORK ASSISTANT
# ----------------------------------

elif menu == "Homework Assistant":

    st.header("📖 AI Homework Assistant")

    subject = st.selectbox(
        "Select your subject",
        [
            "Mathematics",
            "English",
            "Biology",
            "Chemistry",
            "Physics",
            "Other"
        ]
    )

    question = st.text_area(
        "Enter your homework question",
        placeholder="Type your question here..."
    )

    if st.button("Submit Question"):

        if question.strip():

            st.write("**Subject:**", subject)

            st.info(
                "Your question has been received. "
                "AI integration is coming in the next phase."
            )

        else:

            st.warning(
                "Please enter a question first."
            )

# ----------------------------------
# 7. EXAM PREPARATION
# ----------------------------------

elif menu == "Exam Preparation":

    st.header("📝 Examination Preparation")

    exam = st.selectbox(
        "Choose your examination",
        ["WAEC", "NECO", "JAMB"]
    )

    subject = st.selectbox(
        "Choose your subject",
        [
            "Mathematics",
            "English",
            "Biology",
            "Chemistry",
            "Physics"
        ]
    )

    st.write("Examination:", exam)
    st.write("Subject:", subject)

    st.info(
        "Practice questions and mock examinations "
        "will be introduced in the next phase."
    )

# ----------------------------------
# 8. MULTILINGUAL LEARNING
# ----------------------------------

elif menu == "Multilingual Learning":

    st.header("🌍 Multilingual Learning")

    language = st.selectbox(
        "Choose your preferred language",
        [
            "English",
            "Hausa",
            "Yoruba",
            "Igbo",
            "Nigerian Pidgin"
        ]
    )

    st.write("Selected language:", language)

    st.info(
        "Multilingual AI support will be connected "
        "in a future development phase."
    )

# ----------------------------------
# 9. STUDY PLANNER
# ----------------------------------

elif menu == "Study Planner":

    st.header("📅 My Study Planner")

    task = st.text_input(
        "What do you want to study?"
    )

    if st.button("Add Study Task"):

        if task.strip():

            st.session_state.tasks.append(
                task.strip()
            )

            st.success("Study task added!")

        else:

            st.warning(
                "Please enter a study task."
            )

    st.subheader("My Learning Tasks")

    if st.session_state.tasks:

        for index, item in enumerate(
            st.session_state.tasks,
            start=1
        ):

            st.write(f"{index}. {item}")

        if st.button("Clear All Tasks"):

            st.session_state.tasks = []

            st.rerun()

    else:

        st.write("You have no study tasks yet.")

# ----------------------------------
# 10. FOOTER
# ----------------------------------

st.divider()

st.caption(
    "EduBridge AI © 2026 | "
    "Empowering Nigerian Students Through AI"
)
