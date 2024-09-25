-- 9 Знайти список курсів, які відвідує студент.
SELECT s.id, s.name, st.id as st_id, st."name" as st_name
FROM subjects s
JOIN grades g ON s.id = g.subject_id
JOIN students st ON st.id = g.student_id 
WHERE g.student_id = 27;



id|name       |st_id|st_name      |
--+-----------+-----+-------------+
 1|Mathematics|   27|Ігнат Колодуб|
 2|Physics    |   27|Ігнат Колодуб|
 3|Geometry   |   27|Ігнат Колодуб|
 4|Programming|   27|Ігнат Колодуб|
 5|Chemistry  |   27|Ігнат Колодуб|
 6|Biology    |   27|Ігнат Колодуб|
 7|History    |   27|Ігнат Колодуб|



-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select s.id, s.name, st.id, st.name 
    from subjects s
    join grades g ON s.id = g.subject_id
    join students st ON st.id = g.student_id 
    where g.student_id = %s	
"""