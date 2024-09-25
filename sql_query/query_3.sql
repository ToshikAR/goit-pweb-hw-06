-- 3 Знайти середній бал у групах з певного предмета.
SELECT g.id, g.name, AVG(gr.grade) AS average_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gr ON s.id = gr.student_id
WHERE gr.subject_id = 2  -- Замініть :subject_id на потрібний ID предмета
GROUP BY g.id, g.name;


id|name  |average_grade     |
--+------+------------------+
 3|GroupC|5.8461538461538462|
 1|GroupA|6.2500000000000000|
 2|GroupB|4.3125000000000000||





-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select g.id, g.name, AVG(gr.grade) AS average_grade
    from groups g
    join students s ON g.id = s.group_id
    join grades gr ON s.id = gr.student_id
    where gr.subject_id = %s
    group by g.id, g.name;
"""