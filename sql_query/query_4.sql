-- 4 Знайти середній бал на потоці (по всій таблиці оцінок).
SELECT AVG(grade) AS average_grade
FROM grades;


average_grade     |
------------------+
6.3523809523809524|




-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select AVG(grade) AS average_grade
    from grades;
"""