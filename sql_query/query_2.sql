-- 2 Знайти студента із найвищим середнім балом з певного предмета.
SELECT s.id, s.name, AVG(g.grade) as average_grad
FROM students s
JOIN grades g ON s.id = g.student_id
WHERE g.subject_id = 1  -- Замініть :subject_id на потрібний ID предмета
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 1;


id|name           |average_grade      |
--+---------------+-------------------+
42|Орися Данильчук|12.0000000000000000|


-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select s.id, s.name, AVG(g.grade) as average_grade 
    from students s
    join grades g ON s.id = g.student_id
    where g.subject_id = %s
    group by s.id, s.name
    order BY average_grade DESC
    limit 1;
"""