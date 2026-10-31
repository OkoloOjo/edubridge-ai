

"""
EduBridge AI - Homework Assistant

Uses Google Gemini AI to help Nigerian
students understand their homework.
"""

import streamlit as st
from google import genai


def validate_question(question):
    """Check whether the student entered a question."""

    if not question or not question.strip():
        return False

    return True


def create_homework_prompt(subject, question, level):
    """Prepare instructions for the AI tutor."""

    prompt = f"""
You are EduBridge AI, a friendly and patient
educational tutor for Nigerian students.

Help the student understand the following question.

Subject: {subject}
Student education level: {level}
Question: {question}

Your instructions:

1. Explain the concept in simple language.
2. Show the solution step by step.
3. Give a practical example.
4. Use examples relevant to everyday Nigerian life
   where appropriate.
5. Encourage the student to understand the answer.
6. Explain difficult words.
7. Do not invent facts.
8. Adjust your explanation to the student's level.

Be friendly, accurate and educational.
"""

    return prompt


def get_homework_response(question, subject, level):
    """Generate an actual AI homework explanation."""

    if not validate_question(question):
        return "Please enter a valid homework question."

    try:
        api_key = st.secrets["GEMINI_API_KEY"]

        client = genai.Client(api_key=api_key)

        prompt = create_homework_prompt(
            subject,
            question,
            level
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        if not response.text:
            return "The AI could not generate an answer. Please try again."

        return response.text

    except KeyError:
        return (
            "Gemini API key is missing. "
            "Please configure GEMINI_API_KEY in Streamlit Secrets."
        )

    except Exception:
        return (
            "Sorry, EduBridge AI could not generate "
            "a response right now. Please try again later."
        )
