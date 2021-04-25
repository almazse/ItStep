CREATE TABLE Album
   (
       id INTEGER,
       name CHAR(45),
       id_artist INTEGER,
       year_album INTEGER,
       charts INTEGER
   );

INSERT INTO Album (id, name, id_artist, year_album, charts) VALUES
    (1, "Lorem ", 1, 1991, 20),
    (2, "ipsum ", 1, 1992, 30),
    (3, "dolor ", 1, 1992, 50),
    (4, "sit ", 1, 1993, 100),
    (5, "amet ", 2, 2000, 80),
    (6, "consectetur ", 2, 2002, 70),
    (7, "adipiscing ", 2, 2005, 90),
    (8, "elit ", 3, 2005, 90),
    (9, "sed ", 4, 2005, 80),
    (10, "eiusmod ", 5, 2005, 80),
    (11, "tempor ", 6, 2005, 80),
    (12, "incididunt ", 7, 2005, 80),
    (13, "labore ", 7, 2020, 30),
    (14, "dolore ", 8, 2021, 100);

CREATE TABLE Artist
   (
       id INTEGER,
       name CHAR(40),
       id_genre INTEGER
   );

INSERT INTO Artist (id, name, id_genre) VALUES
    (1, "Poll", 1),
    (2, "Britany", 2),
    (3, "Till", 3),
    (4, "Bobby", 1),
    (5, "Jorj", 4),
    (6, "Polo", 5),
    (7, "Drake", 5),
    (8, "Luce", 5);

CREATE TABLE Genre
   (
       id INTEGER,
       name CHAR(40)
   );

INSERT INTO Genre (id, name) VALUES
    (1, "Rock"),
    (2, "Pop"),
    (3, "Electro"),
    (4, "Jazz"),
    (5, "Hip hop");

--SELECT * FROM Album;
--SELECT * FROM Artist;
--SELECT * FROM Genre;

SELECT Artist.name, Genre.name
FROM Artist
INNER JOIN Genre
ON Artist.id_genre = Genre.id
ORDER BY Artist.name DESC;

SELECT Album.name, Album.year_album, Artist.name
FROM Album
INNER JOIN Artist
ON Artist.id = Album.id_artist;

SELECT Artist.name
FROM Genre
INNER JOIN Artist
ON Genre.id = Artist.id_genre
WHERE Genre.name = "Rock";

SELECT Genre.name as genre, COUNT(Artist.id) as amount
FROM Genre
INNER JOIN Artist
ON Genre.id = Artist.id_genre
GROUP BY Genre.name
ORDER BY 2 ASC;

SELECT Artist.name as name, SUM(Album.charts) as charts
FROM Artist
INNER JOIN Album
ON Album.id_artist = Artist.id
GROUP BY Artist.name
ORDER BY 2 DESC;

SELECT Artist.name, COUNT(Album.id)
FROM Artist
INNER JOIN Album
ON Album.id_artist = Artist.id
GROUP BY Artist.name;

SELECT Genre.name, SUM(Album.charts)
FROM Artist
INNER JOIN Genre
ON Genre.id = Artist.id_genre
INNER JOIN Album
ON Album.id_artist = Artist.id
GROUP BY Artist.id_genre
ORDER BY 2 DESC;

SELECT Artist.name, Album.name
FROM Artist
INNER JOIN Album
ON Album.id_artist = Artist.id
ORDER BY Album.charts DESC
LIMIT 1;

SELECT Artist.name as artist, Album.name as album
FROM Album INNER JOIN Artist
ON Album.id_artist = Artist.id
WHERE Album.charts = (
    SELECT MAX(Album.charts)
    FROM Album
    );