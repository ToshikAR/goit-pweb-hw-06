-- 7 Знайти оцінки студентів у окремій групі з певного предмета.
SELECT s.id, s.name, g.grade, sb.name AS sub_name
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sb ON g.subject_id = sb.id
WHERE s.group_id = 1
  AND g.subject_id = 3;


id|name                 |grade|sub_name|
--+---------------------+-----+--------+
 1|Людмила Гайденко     |    3|Geometry|
 8|Гліб Супруненко      |    1|Geometry|
 9|Єлисавета Фесенко    |    3|Geometry|
12|Оксана Алексійчук    |    8|Geometry|
16|Стефан Яковенко      |    1|Geometry|
23|Розалія Орлик        |    4|Geometry|
24|Микита Засуха        |    4|Geometry|
32|Франц Шинкаренко     |    4|Geometry|
35|Йосип Цибуленко      |   12|Geometry|
39|Єва Масляк           |   12|Geometry|
41|Борислав Міщенко     |   12|Geometry|
42|Орися Данильчук      |    2|Geometry|
46|Олександр Забарний   |    7|Geometry|
47|пані Галина Архимович|    8|Geometry|
49|Юхим Перебийніс      |    6|Geometry|



-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select s.id, s.name, g.grade, sb.name AS sub_name
    from students s
    join grades g on s.id = g.student_id
    join subjects sb on g.subject_id = sb.id
    where s.group_id = %s and g.subject_id = %s
"""