
"""
EduBridge AI
An AI-powered learning assistant for Nigerian students.
"""
import time 

import streamlit as st

from modules.homework import (
    get_homework_response,
    validate_question
)

from modules.exams import (
    get_practice_questions,
    calculate_score,
    get_feedback
)

from modules.languages import (
    get_supported_languages,
    prepare_learning_content
)

from modules.planner import (
    add_study_task,
    complete_study_task,
    delete_study_task,
    get_study_progress
)


# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="EduBridge AI",
    page_icon="📚",
    layout="wide"
)


# --------------------------------
# SESSION STATE
# --------------------------------

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "exam_results" not in st.session_state:
    st.session_state.exam_results = []


# --------------------------------
# APPLICATION HEADER
# --------------------------------

st.title("📚 EduBridge AI")

st.subheader("Your Smart Learning Assistant")

st.write(
    "Learn better. Prepare smarter. Succeed together."
)


# --------------------------------
# SIDEBAR NAVIGATION
# --------------------------------

st.sidebar.title("📚 EduBridge AI")

st.sidebar.write(
    "Your learning companion."
)

menu = st.sidebar.selectbox(
    "Choose a learning feature",
    [
        "Home",
        "AI Homework Assistant",
        "Exam Preparation",
        "Multilingual Learning",
        "Study Planner"
    ]
)


# --------------------------------
# HOME PAGE
# --------------------------------

if menu == "Home":

    st.header("Welcome to EduBridge AI 🇳🇬")

    st.write(
        "Your personal AI-powered education platform."
    )

    st.info(
        "Get homework help, prepare for examinations "
        "and organise your studies."
    )

    st.subheader("What can you do here?")

    col1, col2 = st.columns(2)

    with col1:
        st.success("📖 Get AI-powered homework explanations")
        st.success("📝 Practise examination questions")

    with col2:
        st.success("🌍 Explore multilingual learning")
        st.success("📅 Organise your study activities")

    st.subheader("Your Study Overview")

    progress = get_study_progress(
        st.session_state.tasks
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Tasks",
        progress["total_tasks"]
    )

    col2.metric(
        "Completed",
        progress["completed_tasks"]
    )

    col3.metric(
        "Pending",
        progress["pending_tasks"]
    )


# --------------------------------
# AI HOMEWORK ASSISTANT
# --------------------------------

elif menu == "AI Homework Assistant":

    st.header("📖 AI Homework Assistant")

    st.write(
        "Ask questions and receive step-by-step "
        "explanations from your AI tutor."
    )

    subject = st.selectbox(
        "Choose a subject",
        [
            "Mathematics",
            "English",
            "Physics",
            "Chemistry",
            "Biology",
            "Agricultural Science",
            "Computer Studies",
            "Other"
        ]
    )

    level = st.selectbox(
        "Your education level",
        [
            "Primary School",
            "Junior Secondary School",
            "Senior Secondary School",
            "WAEC / NECO",
            "JAMB",
            "University"
        ]
    )

    question = st.text_area(
        "Enter your homework question",
        placeholder="Example: Explain photosynthesis.",
        height=150
    )

    if st.button(
        "Ask EduBridge AI",
        type="primary"
    ):

        if not validate_question(question):

            st.warning(
                "Please enter a homework question."
            )

        else:

            with st.spinner(
                "EduBridge AI is thinking..."
            ):

                response = get_homework_response(
                    question,
                    subject,
                    level
                )

            st.subheader("🤖 Your AI Tutor's Response")

            st.markdown(response)


# --------------------------------
# EXAM PREPARATION
# --------------------------------

elif menu == "Exam Preparation":

    st.header("📝 Examination Preparation")

    st.write(
        "Practise questions to improve your performance."
    )

    exam = st.selectbox(
        "Choose your examination",
        ["WAEC", "NECO", "JAMB"]
    )

    subject = st.selectbox(
        "Choose a subject",
        ["Mathematics"]
    )

    questions = get_practice_questions(subject)

    if questions:

        st.subheader(
            f"{exam} {subject} Practice"
        )

        with st.form("exam_form"):

            answers = []

            for index, question in enumerate(questions):

                st.write(
                    f"**Question {index + 1}: "
                    f"{question['question']}**"
                )

                answer = st.radio(
                    "Select your answer",
                    question["options"],
                    key=f"answer_{exam}_{index}"
                )

                answers.append(answer)

            submitted = st.form_submit_button(
                "Submit Answers"
            )

        if submitted:

            score = calculate_score(
                questions,
                answers
            )

            st.subheader("Your Results")

            st.metric(
                "Your Score",
                f"{score}%"
            )

            st.write(get_feedback(score))

            for index, question in enumerate(questions):

                if answers[index] == question["answer"]:

                    st.success(
                        f"Question {index + 1}: Correct!"
                    )

                else:

                    st.error(
                        f"Question {index + 1}: "
                        f"Correct answer: {question['answer']}"
                    )

                st.caption(
                    question["explanation"]
                )

    else:

        st.warning(
            "Practice questions are not available yet."
        )


# --------------------------------
# MULTILINGUAL LEARNING
# --------------------------------

elif menu == "Multilingual Learning":

    st.header("🌍 Multilingual Learning")

    st.write(
        "Explore educational content in languages "
        "you understand."
    )

    languages = get_supported_languages()

    language = st.selectbox(
        "Choose your preferred language",
        languages
    )

    content = st.text_area(
        "Enter the learning content"
    )

    if st.button("Prepare Translation"):

        result = prepare_learning_content(
            content,
            language
        )

        if result.startswith("Please"):

            st.warning(result)

        else:

            st.success(
                "Your translation instructions are ready."
            )

            st.info(
                "Actual AI translation is a future integration."
            )

            with st.expander("View translation instructions"):

                st.text(result)


# --------------------------------
# STUDY PLANNER
# --------------------------------

elif menu == "Study Planner":

    st.header("📅 My Study Planner")

    st.write(
        "Create study tasks and monitor your progress."
    )

    with st.form("study_task_form"):

        subject = st.text_input("Subject")

        topic = st.text_input(
            "What do you want to study?"
        )

        study_date = st.date_input("Study date")

        add_task = st.form_submit_button(
            "Add Study Task"
        )

    if add_task:

        previous_count = len(
            st.session_state.tasks
        )

        add_study_task(
            st.session_state.tasks,
            subject,
            topic,
            study_date
        )

        if len(st.session_state.tasks) > previous_count:

            st.success(
                "Study task added successfully!"
            )

        else:

            st.warning(
                "Please enter both subject and topic."
            )

    st.divider()

    st.subheader("My Study Tasks")

    if not st.session_state.tasks:

        st.info("You have no study tasks yet.")

    else:

        for index, task in enumerate(
            st.session_state.tasks
        ):

            col1, col2, col3 = st.columns([3, 2, 1])

            with col1:

                if task["completed"]:

                    st.write(
                        f"~~{task['subject']}: "
                        f"{task['topic']}~~"
                    )

                else:

                    st.write(
                        f"**{task['subject']}**: "
                        f"{task['topic']}"
                    )

                st.caption(
                    f"Study date: {task['study_date']}"
                )

            with col2:

                if not task["completed"]:

                    if st.button(
                        "Mark Complete",
                        key=f"complete_{index}"
                    ):

                        complete_study_task(
                            st.session_state.tasks,
                            index
                        )

                        st.rerun()

                else:

                    st.success("Completed")

            with col3:

                if st.button(
                    "Delete",
                    key=f"delete_{index}"
                ):

                    delete_study_task(
                        st.session_state.tasks,
                        index
                    )

                    st.rerun()

    st.divider()

    st.subheader("Study Progress")

    progress = get_study_progress(
        st.session_state.tasks
    )

    st.progress(
        progress["progress_percentage"] / 100
    )

    st.write(
        f"Progress: {progress['progress_percentage']}%"
    )

    st.write(
        f"Completed: {progress['completed_tasks']} "
        f"of {progress['total_tasks']} tasks"
    )


# --------------------------------
# FOOTER
# --------------------------------

st.sidebar.divider()

st.sidebar.caption(
    "EduBridge AI | Built for Nigerian learners 🇳🇬"
)
