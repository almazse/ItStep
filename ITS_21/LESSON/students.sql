CREATE TABLE Students
   (
       id INTEGER,
       surname CHAR(15),
       id_group INTEGER
   );

INSERT INTO Students (id, surname, id_group) VALUES
    (111, "Semenov", 1),
    (112, "Leshukov", 2),
    (114, "Ivanov", 3),
    (117, "Stoyanovskiy", 3);

--SELECT * FROM Students;

CREATE TABLE Groups
(
    id INTEGER,
    group_name CHAR(15),
    id_facult INTEGER
);

INSERT INTO Groups (id, group_name, id_facult) VALUES
(1, "K-18", 11),
(2, "K-20", 11),
(3, "F-22", 12);

--SELECT * FROM Groups;

CREATE TABLE Faculty
(
    id INTEGER,
    faculty_name CHAR(15)
);

INSERT INTO Faculty (id, faculty_name) VALUES
(11, "KT"),
(12, "FK");

--SELECT * FROM Faculty;

CREATE TABLE Subject
(
    id INTEGER,
    subject_name CHAR(15)
);

INSERT INTO Subject (id, subject_name) VALUES
(101, "Phisics"),
(102, "Computer science"),
(103, "Math");

--SELECT * FROM Subject;

CREATE TABLE Journal
(
    id INTEGER,
    id_student INTEGER,
    id_subject INTEGER,
    mark INTEGER
);

INSERT INTO Journal (id, id_student, v, mark) VALUES
(101, 111, 101, 60),
(102, 111, 102, 80),
(103, 112, 101, 70),
(104, 112, 102, 90),
(105, 114, 103, 75),
(106, 117, 101, 75),
(107, 117, 102, 85);

--SELECT * FROM Journal;

SELECT surname, id_group FROM Students;

SELECT * FROM Students ORDER BY surname DESC;

SELECT mark FROM Journal WHERE id_student = 111 AND id_subject = 102;

SELECT mark FROM Journal WHERE id_student = 114 AND id_subject = 101;

SELECT Students.surname, Groups.group_name
FROM Students
INNER JOIN Groups
ON Students.id_group = Groups.id;

SELECT Groups.group_name, Faculty.faculty_name
FROM Faculty
INNER JOIN Groups
ON Faculty.id = Groups.id_facult;

SELECT Groups.group_name, Faculty.faculty_name, Students.surname
FROM Students INNER JOIN Groups
ON Students.id_group = Groups.id
INNER JOIN Faculty
ON Faculty.id = Groups.id_facult
ORDER BY Students.surname;

SELECT COUNT(mark)
FROM Journal
WHERE id_student = 112;

SELECT id_subject, AVG(mark) as "average_mark"
FROM Journal
GROUP BY id_subject
ORDER BY AVG(mark) DESC;

SELECT Subject.subject_name as "subject", AVG(mark) as "averege_matk"
FROM Journal
INNER JOIN Subject
ON Subject.id = Journal.id_subject
GROUP BY Subject.subject_name
ORDER BY AVG(mark) DESC;

SELECT Students.surname as "student", MIN(mark) as "min_mark"
FROM Journal
INNER JOIN Students
ON Students.id = Journal.id_student
GROUP BY student
ORDER BY 1;

SELECT Groups.group_name, AVG(mark) as "arg_mark"
FROM Journal
INNER JOIN Students
ON Students.id = Journal.id_student
INNER JOIN Groups
ON Students.id_group = Groups.id
GROUP BY Groups.group_name
ORDER BY 2 DESC;

SELECT Students.surname, Groups.group_name
FROM Students
INNER JOIN Groups
ON Students.id_group = Groups.id
WHERE Students.surname LIKE "S%";

SELECT Students.surname, Groups.group_name
FROM Students
INNER JOIN Groups
ON Students.id_group = Groups.id
WHERE Students.surname LIKE "%ov";

SELECT Students.surname, Subject.subject_name, Journal.mark
FROM Journal
INNER JOIN Subject
ON Subject.id = Journal.id_subject
INNER JOIN Students
ON Students.id = Journal.id_student
WHERE Journal.mark IN (80, 90);

SELECT Students.surname, Subject.subject_name, Journal.mark
FROM Journal
INNER JOIN Subject
ON Subject.id = Journal.id_subject
INNER JOIN Students
ON Students.id = Journal.id_student
WHERE Journal.mark BETWEEN 60 AND 75;

SELECT Students.surname, Subject.subject_name, MAX(Journal.mark)
FROM Journal
INNER JOIN Subject
ON Subject.id = Journal.id_subject
INNER JOIN Students
ON Students.id = Journal.id_student
GROUP BY Students.surname
ORDER BY 3 DESC
LIMIT 3;