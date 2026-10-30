
"""
EduBridge AI - Database Module

Manages student records, examination results
and study tasks using SQLite.
"""

import sqlite3
from pathlib import Path


# Database location
BASE_DIR = Path(__file__).resolve().parent

DB_PATH = BASE_DIR / "edubridge.db"


def get_connection():
    """Create a connection to the database."""

    connection = sqlite3.connect(DB_PATH)

    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """Create all required database tables."""

    with get_connection() as connection:

        # Students table
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        # Examination results table
        connection.execute("""
            CREATE TABLE IF NOT EXISTS exam_results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                exam_type TEXT NOT NULL,
                subject TEXT NOT NULL,
                score REAL NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id)
                    REFERENCES students(id)
            )
        """)

        # Study tasks table
        connection.execute("""
            CREATE TABLE IF NOT EXISTS study_tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                subject TEXT NOT NULL,
                topic TEXT NOT NULL,
                study_date TEXT NOT NULL,
                completed INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (student_id)
                    REFERENCES students(id)
            )
        """)

        connection.execute(
            "PRAGMA foreign_keys = ON"
        )


def add_student(name, email):
    """Register a new student."""

    if not name.strip() or not email.strip():
        raise ValueError("Name and email are required.")

    try:
        with get_connection() as connection:

            cursor = connection.execute(
                """
                INSERT INTO students (name, email)
                VALUES (?, ?)
                """,
                (name.strip(), email.strip().lower())
            )

            return cursor.lastrowid

    except sqlite3.IntegrityError:
        raise ValueError(
            "A student with this email already exists."
        )


def get_student(student_id):
    """Retrieve a student using their ID."""

    with get_connection() as connection:

        student = connection.execute(
            """
            SELECT * FROM students
            WHERE id = ?
            """,
            (student_id,)
        ).fetchone()

        return dict(student) if student else None


def add_exam_result(
    student_id,
    exam_type,
    subject,
    score
):
    """Save a student's examination result."""

    if not 0 <= score <= 100:
        raise ValueError("Score must be between 0 and 100.")

    with get_connection() as connection:

        cursor = connection.execute(
            """
            INSERT INTO exam_results (
                student_id,
                exam_type,
                subject,
                score
            )
            VALUES (?, ?, ?, ?)
            """,
            (student_id, exam_type, subject, score)
        )

        return cursor.lastrowid


def get_exam_results(student_id):
    """Retrieve examination results for a student."""

    with get_connection() as connection:

        results = connection.execute(
            """
            SELECT * FROM exam_results
            WHERE student_id = ?
            ORDER BY created_at DESC
            """,
            (student_id,)
        ).fetchall()

        return [dict(result) for result in results]


def add_database_task(
    student_id,
    subject,
    topic,
    study_date
):
    """Save a study task."""

    with get_connection() as connection:

        cursor = connection.execute(
            """
            INSERT INTO study_tasks (
                student_id,
                subject,
                topic,
                study_date
            )
            VALUES (?, ?, ?, ?)
            """,
            (student_id, subject, topic, str(study_date))
        )

        return cursor.lastrowid


def get_database_tasks(student_id):
    """Retrieve a student's study tasks."""

    with get_connection() as connection:

        tasks = connection.execute(
            """
            SELECT * FROM study_tasks
            WHERE student_id = ?
            ORDER BY study_date ASC
            """,
            (student_id,)
        ).fetchall()

        return [dict(task) for task in tasks]


def complete_database_task(task_id, student_id):
    """Mark a student's task as completed."""

    with get_connection() as connection:

        cursor = connection.execute(
            """
            UPDATE study_tasks
            SET completed = 1
            WHERE id = ? AND student_id = ?
            """,
            (task_id, student_id)
        )

        return cursor.rowcount > 0
