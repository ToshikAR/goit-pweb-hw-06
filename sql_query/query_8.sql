-- 8 Знайти середній бал, який ставить певний викладач зі своїх предметів.
SELECT t.name AS teacher_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects s ON g.subject_id = s.id
JOIN teachers t ON s.teacher_id = t.id
WHERE t.id = 3
GROUP BY t.name;


teacher_name      |average_grade     |
------------------+------------------+
Вʼячеслав Єрошенко|5.7802197802197802|



-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select  t.name, AVG(g.grade)
    from grades g
    join subjects s ON g.subject_id = s.id
    join teachers t ON s.teacher_id = t.id
    where t.id = %s
    group by t.name;
"""