
"""
EduBridge AI - Homework Assistant

Uses Google Gemini AI to help Nigerian
students understand their homework.
"""
import time 

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
    """Generate an AI homework explanation with retries."""

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

        for attempt in range(3):

            try:
                response = client.models.generate_content(
                    model="gemini-3.8-flash",
                    contents=prompt
                )

                if response.text:
                    return response.text

                return "The AI could not generate an answer. Please try again."

            except Exception as error:

                error_message = str(error)

                if "503" in error_message or "UNAVAILABLE" in error_message:

                    if attempt < 2:
                        wait_time = 2 ** (attempt + 1)

                        time.sleep(wait_time)

                    else:
                        return (
                            "Gemini is currently experiencing high demand. "
                            "Please wait a little and try again."
                        )

                else:
                    raise error

    except KeyError:
        return "Gemini API key is missing. Check Streamlit Secrets."

    except Exception as error:
        st.error(
            f"Gemini Error: {type(error).__name__}: {error}"
        )

        return "EduBridge AI could not generate an answer. Please try again."
