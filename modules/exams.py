
"""
EduBridge AI - Examination Preparation Module

Provides practice questions, answer checking
and examination scoring.
"""

# Original practice questions
# These are demonstration questions, not official past questions.

QUESTION_BANK = {

    "Mathematics": [

        {
            "question": "What is 12 × 8?",
            "options": ["86", "96", "108", "112"],
            "answer": "96",
            "explanation": "12 multiplied by 8 equals 96."
        },

        {
            "question": "What is 25% of 200?",
            "options": ["25", "40", "50", "75"],
            "answer": "50",
            "explanation": "25% of 200 = (25/100) × 200 = 50."
        },

        {
            "question": "Solve: 15 + 27.",
            "options": ["32", "40", "42", "45"],
            "answer": "42",
            "explanation": "15 + 27 = 42."
        }
    ]
}


def get_practice_questions(subject):
    """Return questions for the selected subject."""

    return QUESTION_BANK.get(subject, [])


def check_answer(question, selected_answer):
    """Check whether a student's answer is correct."""

    correct_answer = question["answer"]

    return selected_answer == correct_answer


def calculate_score(questions, student_answers):
    """Calculate the student's examination score."""

    if not questions:
        return 0

    correct = 0

    for question, answer in zip(
        questions,
        student_answers
    ):

        if check_answer(question, answer):
            correct += 1

    percentage = (correct / len(questions)) * 100

    return round(percentage, 2)


def get_feedback(score):
    """Provide feedback based on examination performance."""

    if score >= 80:
        return "Excellent performance! Keep it up."

    elif score >= 60:
        return "Good work! Keep practising."

    elif score >= 40:
        return "Fair performance. More practice will help."

    else:
        return "Keep learning. You can improve!"
