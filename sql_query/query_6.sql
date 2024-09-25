-- # 6 Знайти список студентів у певній групі.
SELECT s.id , s.name, g.name
FROM students s
JOIN groups g ON s.group_id = g.id
WHERE s.group_id  = 1;



id|name                 |name  |
--+---------------------+------+
 1|Людмила Гайденко     |GroupA|
 8|Гліб Супруненко      |GroupA|
 9|Єлисавета Фесенко    |GroupA|
12|Оксана Алексійчук    |GroupA|
16|Стефан Яковенко      |GroupA|
23|Розалія Орлик        |GroupA|
24|Микита Засуха        |GroupA|
32|Франц Шинкаренко     |GroupA|
35|Йосип Цибуленко      |GroupA|
37|Єлисавета Чуйко      |GroupA|
38|Веніямин Їжакевич    |GroupA|
39|Єва Масляк           |GroupA|
41|Борислав Міщенко     |GroupA|
42|Орися Данильчук      |GroupA|
46|Олександр Забарний   |GroupA|
47|пані Галина Архимович|GroupA|
49|Юхим Перебийніс      |GroupA|


-- тіло запиту через cursor.execute(sql_expression) буде виглядати так
sql_expression = """
    select s.id, s.name, g.name
    from students s
    join groups g ON s.group_id = g.id
    where group_id  = %s
"""