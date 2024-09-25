"""
Зробити такі вибірки з отриманої бази даних:
    1.Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    2.Знайти студента із найвищим середнім балом з певного предмета.
    3.Знайти середній бал у групах з певного предмета.
    4.Знайти середній бал на потоці (по всій таблиці оцінок).
    5.Знайти які курси читає певний викладач.
    6.Знайти список студентів у певній групі.
    7.Знайти оцінки студентів у окремій групі з певного предмета.
    8.Знайти середній бал, який ставить певний викладач зі своїх предметів.
    9.Знайти список курсів, які відвідує студент.
    10.Список курсів, які певному студенту читає певний викладач.
Для додаткового завдання зробіть такі запити підвищеної складності:
    D1.Середній бал, який певний викладач ставить певному студентові.
    D2.Оцінки студентів у певній групі з певного предмета на останньому занятті.
"""

import logging
from decorator import decorator_sql_query


# 1 Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
@decorator_sql_query
def sql_query_1(cur):
    sql_expression = """
        select s.id, s.name, AVG(g.grade) as average_grade 
        from students s
        join grades g ON s.id = g.student_id
        group by s.id, s.name
        order BY average_grade DESC
        limit 5;
        """
    cur.execute(sql_expression)


# 2 Знайти студента із найвищим середнім балом з певного предмета.
@decorator_sql_query
def sql_query_2(cur, subject_id=1):
    sql_expression = """
        select s.id, s.name, AVG(g.grade) as average_grade 
        from students s
        join grades g ON s.id = g.student_id
        where g.subject_id = %s
        group by s.id, s.name
        order BY average_grade DESC
        limit 1;
    """
    cur.execute(sql_expression, (subject_id,))


# 3 Знайти середній бал у групах з певного предмета.
@decorator_sql_query
def sql_query_3(cur, subject_id=1):
    sql_expression = """
        select g.id, g.name, AVG(gr.grade) AS average_grade
        from groups g
        join students s ON g.id = s.group_id
        join grades gr ON s.id = gr.student_id
        where gr.subject_id = %s
        group by g.id, g.name;
    """
    cur.execute(sql_expression, (subject_id,))


# 4 Знайти середній бал на потоці (по всій таблиці оцінок).
@decorator_sql_query
def sql_query_4(cur):
    sql_expression = """
        select AVG(grade) AS average_grade
        from grades;
    """
    cur.execute(sql_expression)


# 5 Знайти які курси читає певний викладач.
@decorator_sql_query
def sql_query_5(cur, teacher_id=1):
    sql_expression = """
        select s.id, s.name, t."name" 
        from subjects s
        join teachers t ON s.teacher_id = t.id
        where t.id = %s
    """
    cur.execute(sql_expression, (teacher_id,))


# 6 Знайти список студентів у певній групі.
@decorator_sql_query
def sql_query_6(cur, group_id=1):
    sql_expression = """
        select s.id, s.name, g.name
        from students s
        join groups g ON s.group_id = g.id
        where group_id  = %s
    """
    cur.execute(sql_expression, (group_id,))


# 7 Знайти оцінки студентів у окремій групі з певного предмета.
@decorator_sql_query
def sql_query_7(cur, group_id=1, subject_id=1):
    sql_expression = """
        select s.id, s.name, g.grade, sb.name
        from students s
        join grades g on s.id = g.student_id
        join subjects sb on g.subject_id = sb.id
        where s.group_id = %s and g.subject_id = %s
    """
    cur.execute(sql_expression, (group_id, subject_id))


# 8 Знайти середній бал, який ставить певний викладач зі своїх предметів.
@decorator_sql_query
def sql_query_8(cur, teacher_id=1):
    sql_expression = """
        select  t.name, AVG(g.grade)
        from grades g
        join subjects s on g.subject_id = s.id
        join teachers t on s.teacher_id = t.id
        where t.id = %s
        group by t.name;
    """
    cur.execute(sql_expression, (teacher_id,))


# 9 Знайти список курсів, які відвідує студент.
@decorator_sql_query
def sql_query_9(cur, student_id=1):
    sql_expression = """
        select s.id, s.name, st.id, st.name 
        from subjects s
        join grades g ON s.id = g.subject_id
        join students st ON st.id = g.student_id 
        where g.student_id = %s	
    """
    cur.execute(sql_expression, (student_id,))


# 10 Список курсів, які певному студенту читає певний викладач.
@decorator_sql_query
def sql_query_10(cur, student_id=1, teacher_id=1):
    sql_expression = """
        select s.id, s.name, t.name, st."name"e
        from subjects s
        join grades g on s.id = g.subject_id
        join teachers t on s.teacher_id = t.id
        join students st on st.id = g.student_id
        where g.student_id = %s and t.id = %s
    """
    cur.execute(sql_expression, (student_id, teacher_id))


# D1 Середній бал, який певний викладач ставить певному студентові.
@decorator_sql_query
def sql_query_D1(cur, student_id=1, teacher_id=1):
    sql_expression = """
        select t.name, s.name, AVG(g.grade)
        from grades g
        join subjects sub ON g.subject_id = sub.id
        join teachers t ON sub.teacher_id = t.id
        join students s ON g.student_id = s.id
        where g.student_id = %s and t.id = %s
        group by t.name, s.name;
    """
    cur.execute(sql_expression, (student_id, teacher_id))


# D2.Оцінки студентів у певній групі з певного предмета на останньому занятті.
@decorator_sql_query
def sql_query_D2(cur, groups_id=1, subject_id=1):
    sql_expression = """
        select s.id,  s.name, sub.name, gr.name, g.date_received
        from grades g
        join students s on g.student_id = s.id
        join subjects sub on g.subject_id = sub.id
        join groups gr on s.group_id = gr.id 
        where gr.id = %s and sub.id = %s;
    """
    cur.execute(sql_expression, (groups_id, subject_id))


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s %(module)s %(message)s")
    # result = sql_query_1()
    # result = sql_query_2()
    # result = sql_query_3()
    # result = sql_query_4()
    # result = sql_query_5()
    # result = sql_query_6(2)
    # result = sql_query_7(1, 3)
    # result = sql_query_8(3)
    # result = sql_query_9(27)
    # result = sql_query_10(17, 3)
    # result = sql_query_D1(45, 3)
    result = sql_query_D2(1, 2)

    print(result)
