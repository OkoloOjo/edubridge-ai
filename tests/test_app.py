
"""
EduBridge AI - Automated Tests

Tests the application's main modules.
"""

import pytest

from modules.homework import (
    validate_question,
    create_homework_prompt
)

from modules.exams import (
    get_practice_questions,
    check_answer,
    calculate_score,
    get_feedback
)

from modules.languages import (
    get_supported_languages,
    validate_language
)

from modules.planner import (
    create_study_task,
    complete_study_task,
    get_study_progress
)

from utils.security import (
    validate_name,
    validate_email,
    validate_student_input,
    validate_text_input
)


# ----------------------------------
# HOMEWORK TESTS
# ----------------------------------

def test_homework_question_validation():

    assert validate_question("What is AI?") is True

    assert validate_question("") is False


def test_homework_prompt():

    prompt = create_homework_prompt(
        "Mathematics",
        "What is 2 + 2?",
        "Secondary School"
    )

    assert "Mathematics" in prompt
    assert "What is 2 + 2?" in prompt


# ----------------------------------
# EXAMINATION TESTS
# ----------------------------------

def test_get_practice_questions():

    questions = get_practice_questions("Mathematics")

    assert len(questions) > 0


def test_check_answer():

    question = {
        "question": "What is 2 + 2?",
        "answer": "4"
    }

    assert check_answer(question, "4") is True

    assert check_answer(question, "5") is False


def test_calculate_score():

    questions = [
        {"answer": "A"},
        {"answer": "B"},
        {"answer": "C"}
    ]

    answers = ["A", "B", "C"]

    score = calculate_score(questions, answers)

    assert score == 100.0


def test_exam_feedback():

    assert "Excellent" in get_feedback(90)


# ----------------------------------
# LANGUAGE TESTS
# ----------------------------------

def test_supported_languages():

    languages = get_supported_languages()

    assert "English" in languages
    assert "Hausa" in languages
    assert "Yoruba" in languages
    assert "Igbo" in languages


def test_language_validation():

    assert validate_language("English") is True

    assert validate_language("French") is False


# ----------------------------------
# STUDY PLANNER TESTS
# ----------------------------------

def test_create_study_task():

    task = create_study_task(
        "Mathematics",
        "Algebra",
        "2026-11-01"
    )

    assert task["subject"] == "Mathematics"
    assert task["completed"] is False


def test_complete_study_task():

    tasks = [
        {"completed": False}
    ]

    complete_study_task(tasks, 0)

    assert tasks[0]["completed"] is True


def test_study_progress():

    tasks = [
        {"completed": True},
        {"completed": False}
    ]

    progress = get_study_progress(tasks)

    assert progress["total_tasks"] == 2
    assert progress["completed_tasks"] == 1
    assert progress["progress_percentage"] == 50.0


# ----------------------------------
# SECURITY TESTS
# ----------------------------------

def test_validate_name():

    assert validate_name("Ojonugwa") is True

    assert validate_name("") is False


def test_validate_email():

    assert validate_email("student@example.com") is True

    assert validate_email("invalid-email") is False


def test_validate_student_input():

    valid, message = validate_student_input(
        "John",
        "john@example.com"
    )

    assert valid is True


def test_validate_text_input():

    assert validate_text_input("Hello EduBridge") is True

    assert validate_text_input("") is False

    assert validate_text_input("A" * 3000) is False
