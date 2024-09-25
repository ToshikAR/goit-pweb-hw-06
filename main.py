"""
Реалізуйте базу даних, схема якої містить:

Таблиця студентів;
Таблицю груп;
Таблицю викладачів;
Таблицю предметів із вказівкою викладача, який читає предмет;
Таблицю, де у кожного студента є оцінки з предметів із зазначенням коли оцінку отримано;

Заповніть отриману базу даних випадковими даними (~30-50 студентів, 3 групи, 5-8 предметів, 3-5 викладачів, до 20 оцінок у кожного студента з усіх предметів).

Використовуйте пакет Faker для наповнення.
"""

import time
import logging
import insert_tables as insert
import create_tables as create
import select_sql as query

logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(module)s %(message)s")
isCrFilTab = False


def sql_creating_filling_tables():
    # Створення таблиць у базі module6base PostgreSQL

    # Таблицю груп -groups;
    create.sql_execute(create.sql_create_groups)
    # Таблиця студентів -students;
    create.sql_execute(create.sql_create_students)
    # Таблицю викладачів -teachers;
    create.sql_execute(create.sql_create_teachers)
    # Таблицю предметів із вказівкою викладача, який читає предмет -teachers;
    create.sql_execute(create.sql_create_subjects)
    # Таблицю, де у кожного студента є оцінки з предметів із зазначенням коли оцінку отримано -grades;
    create.sql_execute(create.sql_create_grades)
    time.sleep(5)

    # Заповніть отриману базу даних випадковими даними
    # Використовуйте пакет Faker для наповнення

    # Заповнення таблиць groups
    insert.sql_insert_groups()
    # Заповнення таблиць -students
    insert.sql_insert_students()
    # Заповнення таблиць -teachers
    insert.sql_insert_teachers()
    # Заповнення таблиць -subjects
    insert.sql_insert_subjects()
    # Заповнення таблиць -grades
    insert.sql_insert_grades()


if __name__ == "__main__":
    if isCrFilTab:
        sql_creating_filling_tables()
        time.sleep(5)

    # 10 Список курсів, які певному студенту читає певний викладач.
    result = query.sql_query_10(student_id=17, teacher_id=3)
    print(result)
