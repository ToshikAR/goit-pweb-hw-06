--1 Знайти 5 студентів із найбільшим середнім балом з усіх предметів.

SELECT s.id, s.name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY s.id, s.name
ORDER BY average_grade DESC
LIMIT 5;



id|name              |average_grade     |
--+------------------+------------------+
46|Олександр Забарний|9.0000000000000000|
26|Юхим Гуцуляк      |8.5714285714285714|
 4|Лілія Бабʼюк      |8.5000000000000000|
34|Борислав Ватаманюк|8.2500000000000000|
45|Амалія Рудько     |8.1666666666666667|


-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select s.id, s.name, AVG(g.grade) as average_grade 
    from students s
    join grades g ON s.id = g.student_id
    group by s.id, s.name
    order BY average_grade DESC
    limit 5;
    """