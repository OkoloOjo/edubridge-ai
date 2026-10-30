
"""
EduBridge AI - Multilingual Learning Module

Prepares educational content for translation
and multilingual AI assistance.
"""

SUPPORTED_LANGUAGES = [
    "English",
    "Hausa",
    "Yoruba",
    "Igbo",
    "Nigerian Pidgin"
]


def get_supported_languages():
    return SUPPORTED_LANGUAGES


def validate_language(language):
    return language in SUPPORTED_LANGUAGES


def create_translation_prompt(text, language):

    if not text or not text.strip():
        return None

    if not validate_language(language):
        return None

    prompt = f"""
You are EduBridge AI, a multilingual educational tutor.

Translate the following educational content into
{language}.

Original content:
{text}

Instructions:
1. Preserve the original meaning.
2. Use simple language suitable for students.
3. Keep scientific and mathematical terms accurate.
4. Explain difficult words where necessary.
5. Do not invent information.
6. Make the translation easy to understand.

Return only the translated educational content.
"""

    return prompt


def prepare_learning_content(text, language):

    if not text or not text.strip():
        return "Please enter some learning content."

    if not validate_language(language):
        return "Please select a supported language."

    return create_translation_prompt(text, language)
