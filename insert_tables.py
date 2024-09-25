"""
Заповнення таблиць students, teachers, groups, subjects у базі module6base PostgreSQL
"""

import logging
import random

from faker import Faker

from decorator import decorator_sql_transaction

fake = Faker("uk-UA")

COUNT_STUDENT = 50
COUNT_TEACHERS = 5

SUBJECTE = ["Mathematics", "Physics", "Geometry", "Programming", "Chemistry", "Biology", "History"]
GROUPS = ["GroupA", "GroupB", "GroupC"]

students_id = []
teachers_id = []
groups_id = []
subjects_id = []


# Створення груп
@decorator_sql_transaction
def sql_insert_groups(cur):
    for igroup in GROUPS:
        cur.execute(
            "INSERT INTO groups (name) VALUES (%s) RETURNING id;",
            (igroup,),
        )
        _id = cur.fetchone()
        groups_id.append(_id[0])


# Створення фейкових студентів
@decorator_sql_transaction
def sql_insert_students(cur):
    for _ in range(COUNT_STUDENT):
        cur.execute(
            "INSERT INTO students (name, email, password, age, group_id) VALUES (%s, %s, %s, %s, %s) RETURNING id;",
            (
                fake.name(),
                fake.email(),
                fake.password(),
                random.randint(19, 74),
                random.choice(groups_id),
            ),
        )
        _id = cur.fetchone()
        students_id.append(_id[0])


# Створення фейкових викладачів
@decorator_sql_transaction
def sql_insert_teachers(cur):
    for _ in range(COUNT_TEACHERS):
        cur.execute(
            "INSERT INTO teachers (name, email, password, age) VALUES (%s, %s, %s, %s) RETURNING id;",
            (fake.name(), fake.email(), fake.password(), random.randint(19, 74)),
        )
        _id = cur.fetchone()
        teachers_id.append(_id[0])


# Створення предметів
@decorator_sql_transaction
def sql_insert_subjects(cur):
    for sub in SUBJECTE:
        cur.execute(
            "INSERT INTO subjects (name, teacher_id) VALUES (%s, %s) RETURNING id;",
            (sub, random.choice(teachers_id)),
        )
        _id = cur.fetchone()
        subjects_id.append(_id[0])


# Створення предметів
@decorator_sql_transaction
def sql_insert_grades(cur):
    # Створення фейкових оцінок
    for student_id in students_id:
        # Генеруємо випадкову кількість оцінок від 1 до 20
        num_grades = random.randint(1, 20)
        chosen_subjects = random.sample(
            subjects_id, k=min(num_grades, len(subjects_id))
        )  # Выбираем случайные предметы

        for subject_id in chosen_subjects:
            grade = random.randint(1, 12)  # Генеруємо випадкову оцінку від 1 до 12
            date_received = fake.date_between(
                start_date="-1y", end_date="today"
            )  # Генеруємо випадкову дату в межах року
            cur.execute(
                "INSERT INTO grades (student_id, subject_id, grade, date_received) VALUES (%s, %s, %s, %s);",
                (student_id, subject_id, grade, date_received),
            )


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(module)s %(message)s")

    sql_insert_groups()
    sql_insert_students()
    sql_insert_teachers()
    sql_insert_subjects()
    sql_insert_grades()
