-- 5 Знайти які курси читає певний викладач.
SELECT s.id, s.name, t."name" 
FROM subjects s
JOIN teachers t ON s.teacher_id = t.id
WHERE t.id = 1; -- Замініть :teachers id на потрібний ID



id|name       |name       |
--+-----------+-----------+
 3|Geometry   |Олег Ковпак|
 4|Programming|Олег Ковпак|
 5|Chemistry  |Олег Ковпак|
 7|History    |Олег Ковпак|


-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select s.id, s.name, t."name" 
    from subjects s
    join teachers t ON s.teacher_id = t.id
    where t.id = %s
"""