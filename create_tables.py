"""
Створення таблиць students, teachers, groups, subjects у базі module6base PostgreSQL
"""

import logging
from decorator import decorator_sql_transaction


@decorator_sql_transaction
def sql_execute(cur, sql_expression: str):
    cur.execute(sql_expression)


# Создание таблиці груп
sql_create_groups = """
CREATE TABLE IF NOT EXISTS groups (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);
"""

# Создание таблицы студентів
sql_create_students = """
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    email VARCHAR(120),
    password VARCHAR(120),
    age SMALLINT CHECK (age >= 18 AND age <= 75),
    group_id INT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (group_id) REFERENCES groups(id)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
"""

# Создание таблиці викладачів
sql_create_teachers = """
CREATE TABLE IF NOT EXISTS teachers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    email VARCHAR(120),
    password VARCHAR(120),
    age SMALLINT CHECK (age >= 18 AND age <= 75),
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL
);
"""

# Создание таблиці предметів із вказівкою викладача
sql_create_subjects = """
CREATE TABLE IF NOT EXISTS subjects (
    id SERIAL PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    teacher_id INT,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

# Создание таблиці оцінок студентів з предметів
sql_create_grades = """
CREATE TABLE IF NOT EXISTS grades (
    id SERIAL PRIMARY KEY,
    student_id INT,
    subject_id INT,
    grade INT NOT NULL,
    date_received DATE NOT NULL,
    created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (subject_id) REFERENCES subjects(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(module)s %(message)s")

    # Создание таблиці груп
    sql_execute(sql_create_groups)
    # Создание таблицы студентів
    sql_execute(sql_create_students)
    # Создание таблиці викладачів
    sql_execute(sql_create_teachers)
    # Создание таблиці предметів із вказівкою викладача
    sql_execute(sql_create_subjects)
    # Создание таблиці оцінок студентів з предметів
    sql_execute(sql_create_grades)
