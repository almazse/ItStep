import psycopg2
from settings import *

connection = psycopg2.connect(user=USER, password=PASSWORD,
                              host=HOST, port=PORT, database=DATABASE)

cursor = connection.cursor()

users = """CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    login varchar(50) NOT NULL,
    password varchar(50) NOT NULL,
    first_name varchar(50) NOT NULL,
    last_name varchar(50) NOT NULL,
    role varchar(10) NOT NULL
)"""
cursor.execute(users)
connection.commit()

category = """CREATE TABLE category(
    id SERIAL PRIMARY KEY,
    category_name varchar(50) NOT NULL,
    parent_id INT REFERENCES category(id)
)"""
cursor.execute(category)
connection.commit()

article = """CREATE TABLE article(
    id SERIAL PRIMARY KEY,
    title varchar(200) NOT NULL,
    category INT REFERENCES category(id),
    image varchar(200) NOT NULL,
    text text NOT NULL,
    author INT REFERENCES users(id),
    date_of_publish DATE
)"""
cursor.execute(article)
connection.commit()

comment = """CREATE TABLE comment(
    id SERIAL PRIMARY KEY,
    name varchar(200) NOT NULL,
    text text NOT NULL,
    article_id INT REFERENCES article(id)
)"""
cursor.execute(comment)
connection.commit()

subscriber = """CREATE TABLE subscriber(
    id SERIAL PRIMARY KEY,
    name varchar(200) NOT NULL,
    email varchar(32) NOT NULL
)"""
cursor.execute(subscriber)
connection.commit()


cursor.close()
connection.close()
