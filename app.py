
"""
EduBridge AI
A student learning assistant for Nigerian students.
"""

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


# -----------------------------
# PAGE CONFIGURATION
# -----------------------------

st.set_page_config(
    page_title="EduBridge AI",
    page_icon="📚",
    layout="wide"
)


# -----------------------------
# SESSION STATE
# -----------------------------

if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "exam_results" not in st.session_state:
    st.session_state.exam_results = []


# -----------------------------
# SIDEBAR NAVIGATION
# -----------------------------

st.sidebar.title("📚 EduBridge AI")

st.sidebar.write(
    "Your learning companion."
)

page = st.sidebar.radio(
    "Choose a section",
    [
        "Home",
        "Homework Assistant",
        "Exam Preparation",
        "Multilingual Learning",
        "Study Planner"
    ]
)


# -----------------------------
# HOME PAGE
# -----------------------------

if page == "Home":

    st.title("Welcome to EduBridge AI 🇳🇬")

    st.write(
        "Learn smarter, prepare for examinations "
        "and organise your studies."
    )

    st.subheader("What you can do")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📖 Get help understanding homework.")
        st.info("📝 Practise examination questions.")

    with col2:
        st.info("🌍 Prepare learning content for translation.")
        st.info("📅 Organise your study activities.")

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


# -----------------------------
# HOMEWORK ASSISTANT
# -----------------------------

elif page == "Homework Assistant":

    st.title("📖 Homework Assistant")

    st.write(
        "Enter a question you need help understanding."
    )

    subject = st.selectbox(
        "Choose a subject",
        [
            "Mathematics",
            "English",
            "Physics",
            "Chemistry",
            "Biology",
            "Other"
        ]
    )

    level = st.selectbox(
        "Your education level",
        [
            "Junior Secondary School",
            "Senior Secondary School",
            "WAEC / NECO",
            "JAMB"
        ]
    )

    question = st.text_area(
        "Enter your homework question"
    )

    if st.button("Prepare Homework Help"):

        if not validate_question(question):

            st.warning(
                "Please enter a question first."
            )

        else:

            response = get_homework_response(
                question,
                subject,
                level
            )

            st.success(
                "Your question has been prepared."
            )

            st.info(
                "The AI tutor connection is the next development stage. "
                "This version prepares the instructions but does not "
                "generate an AI answer yet."
            )

            with st.expander("View prepared AI instructions"):

                st.text(response)


# -----------------------------
# EXAM PREPARATION
# -----------------------------

elif page == "Exam Preparation":

    st.title("📝 Examination Preparation")

    st.write(
        "Practise questions to improve your examination performance."
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

            st.write(
                get_feedback(score)
            )

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
            "Practice questions for this subject "
            "are not available yet."
        )


# -----------------------------
# MULTILINGUAL LEARNING
# -----------------------------

elif page == "Multilingual Learning":

    st.title("🌍 Multilingual Learning")

    st.write(
        "Prepare educational content in a language "
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
                "Actual AI translation will be connected "
                "in the next development stage."
            )

            with st.expander("View translation instructions"):

                st.text(result)


# -----------------------------
# STUDY PLANNER
# -----------------------------

elif page == "Study Planner":

    st.title("📅 My Study Planner")

    st.write(
        "Create study tasks and monitor your progress."
    )

    with st.form("study_task_form"):

        subject = st.text_input(
            "Subject"
        )

        topic = st.text_input(
            "What do you want to study?"
        )

        study_date = st.date_input(
            "Study date"
        )

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

        st.info(
            "You have no study tasks yet."
        )

    else:

        for index, task in enumerate(
            st.session_state.tasks
        ):

            col1, col2, col3 = st.columns(
                [3, 2, 1]
            )

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


# -----------------------------
# FOOTER
# -----------------------------

st.sidebar.divider()

st.sidebar.caption(
    "EduBridge AI | Built for Nigerian learners 🇳🇬"
)
