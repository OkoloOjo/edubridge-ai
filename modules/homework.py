
"""
EduBridge AI - Homework Assistant

This module prepares homework questions
for our future AI integration.
"""


def validate_question(question):
    """Check whether the student entered a question."""

    if not question or not question.strip():
        return False

    return True


def create_homework_prompt(subject, question, level):
    """
    Prepare a learning prompt for the AI tutor.
    """

    prompt = f"""
You are EduBridge AI, a friendly educational tutor.

Help a student understand the following question.

Subject: {subject}

Student level: {level}

Question: {question}

Instructions:
1. Explain the concept in simple language.
2. Show the solution step by step.
3. Give a practical example.
4. Encourage the student to understand the answer.
5. Do not simply provide an answer without explanation.

Use language suitable for the student's level.
"""

    return prompt


def get_homework_response(question, subject, level):
    """
    Prepare the question for AI processing.
    """

    if not validate_question(question):
        return "Please enter a valid homework question."

    prompt = create_homework_prompt(
        subject,
        question,
        level
    )

    return prompt
