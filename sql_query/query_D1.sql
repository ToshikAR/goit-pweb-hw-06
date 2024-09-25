-- D1.Середній бал, який певний викладач ставить певному студентові.
SELECT t.name AS teacher_name, s.name AS student_name, AVG(g.grade) AS average_grade
FROM grades g
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON sub.teacher_id = t.id
JOIN students s ON g.student_id = s.id
WHERE g.student_id = 45
  AND t.id = 3
GROUP BY t.name, s.name;


teacher_name      |student_name |average_grade      |
------------------+-------------+-------------------+
Вʼячеслав Єрошенко|Амалія Рудько|11.0000000000000000|



-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select t.name, s.name, AVG(g.grade)
    from grades g
    join subjects sub ON g.subject_id = sub.id
    join teachers t ON sub.teacher_id = t.id
    join students s ON g.student_id = s.id
    where g.student_id = %s and t.id = %s
    group by t.name, s.name;
"""