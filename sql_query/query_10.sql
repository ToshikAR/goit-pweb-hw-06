-- 10 Список курсів, які певному студенту читає певний викладач.
SELECT s.id as sb_id, s.name as sb_name, t.name as th_name, st.name as st_name
FROM subjects s
JOIN grades g ON s.id = g.subject_id
JOIN teachers t ON s.teacher_id = t.id
JOIN students st ON st.id = g.student_id 
WHERE g.student_id = 17 
  AND t.id = 3;


sb_id|sb_name    |th_name           |st_name        |
-----+-----------+------------------+---------------+
    1|Mathematics|Вʼячеслав Єрошенко|Сніжана Височан|
    2|Physics    |Вʼячеслав Єрошенко|Сніжана Височан|



-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select s.id, s.name, t.name, st."name"e
    from subjects s
    join grades g on s.id = g.subject_id
    join teachers t on s.teacher_id = t.id
    join students st on st.id = g.student_id
    where g.student_id = %s and t.id = %s
"""