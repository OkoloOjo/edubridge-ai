
"""
EduBridge AI - Security Module

Provides input validation and safe configuration
handling for the application.
"""

import re
import streamlit as st


def validate_name(name):
    """Validate a student's name."""

    if not isinstance(name, str):
        return False

    name = name.strip()

    if len(name) < 2 or len(name) > 80:
        return False

    if not re.fullmatch(
        r"[A-Za-zÀ-ÖØ-öø-ÿ\s'-]+",
        name
    ):
        return False

    return True


def validate_email(email):
    """Check whether an email address is valid."""

    if not isinstance(email, str):
        return False

    email = email.strip()

    pattern = (
        r"^[A-Za-z0-9._%+-]+@"
        r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
    )

    return bool(re.fullmatch(pattern, email))


def validate_student_input(name, email):
    """Validate student registration information."""

    if not validate_name(name):
        return False, "Please enter a valid name."

    if not validate_email(email):
        return False, "Please enter a valid email address."

    return True, "Student information is valid."


def validate_text_input(text, max_length=2000):
    """Validate general text submitted by users."""

    if not isinstance(text, str):
        return False

    text = text.strip()

    if not text:
        return False

    if len(text) > max_length:
        return False

    return True


def get_secret(secret_name):
    """
    Retrieve sensitive information from
    Streamlit Secrets.
    """

    try:
        secret = st.secrets.get(secret_name)

        if not secret:
            return None

        return secret

    except Exception:
        return None


def mask_secret(secret):
    """Hide sensitive information when displaying it."""

    if not secret:
        return "Not configured"

    return "********"
