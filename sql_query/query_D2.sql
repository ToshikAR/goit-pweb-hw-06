-- D1.Середній бал, який певний викладач ставить певному студентові.
SELECT s.id,  s.name AS student_name, sub.name, gr.name, g.date_received
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON s.group_id = gr.id 
WHERE gr.id = 1
  AND sub.id = 2;




id|student_name         |name   |name  |date_received|
--+---------------------+-------+------+-------------+
 8|Гліб Супруненко      |Physics|GroupA|   2024-06-11|
 9|Єлисавета Фесенко    |Physics|GroupA|   2024-01-05|
12|Оксана Алексійчук    |Physics|GroupA|   2023-11-17|
16|Стефан Яковенко      |Physics|GroupA|   2024-08-03|
23|Розалія Орлик        |Physics|GroupA|   2023-11-18|
24|Микита Засуха        |Physics|GroupA|   2024-08-10|
32|Франц Шинкаренко     |Physics|GroupA|   2024-06-29|
35|Йосип Цибуленко      |Physics|GroupA|   2024-08-03|
37|Єлисавета Чуйко      |Physics|GroupA|   2024-08-31|
38|Веніямин Їжакевич    |Physics|GroupA|   2024-07-29|
39|Єва Масляк           |Physics|GroupA|   2024-01-10|
41|Борислав Міщенко     |Physics|GroupA|   2024-02-22|
42|Орися Данильчук      |Physics|GroupA|   2024-03-26|
46|Олександр Забарний   |Physics|GroupA|   2024-07-02|
47|пані Галина Архимович|Physics|GroupA|   2024-04-28|
49|Юхим Перебийніс      |Physics|GroupA|   2024-05-20|



-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select s.id,  s.name, sub.name, gr.name, g.date_received
    from grades g
    join students s on g.student_id = s.id
    join subjects sub on g.subject_id = sub.id
    join groups gr on s.group_id = gr.id 
    where gr.id = %s and sub.id = %s;
"""