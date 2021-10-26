import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from settings import *

connection = psycopg2.connect(user=USER, password=PASSWORD,
                              host=HOST, port=PORT, database='shop_db')

cursor = connection.cursor()


country = """CREATE TABLE country(
id SERIAL PRIMARY KEY,
country_name varchar(50) NOT NULL
)"""

cursor.execute(country)
cursor.close(country)

city = """CREATE TABLE city(
id SERIAL PRIMARY KEY,
city_name varchar(50) NOT NULL,
country_id INT REFERENCES country(id)
)"""

cursor.execute(city)
cursor.close(city)

customer = """CREATE TABLE customer(
id SERIAL PRIMARY KEY,
city_id INT REFERENCES city(id),
first_name varchar(50) NOT NULL,
last_name varchar(50) NOT NULL
)"""

cursor.execute(customer)
cursor.close(customer)

employee = """CREATE TABLE employee(
id SERIAL PRIMARY KEY,
first_name varchar(50) NOT NULL,
last_name varchar(50) NOT NULL,
date_of_birth DATE,
city_id INT REFERENCES city(id),
chief_id INT REFERENCES employee(id)
)"""

cursor.execute(employee)
cursor.close(employee)

category = """CREATE TABLE product_category(
id SERIAL PRIMARY KEY,
category_name varchar(50) NOT NULL
)"""

cursor.execute(category)
cursor.close(category)

product = """CREATE TABLE product(
id SERIAL PRIMARY KEY,
product_name varchar(50) NOT NULL,
unit_price FLOAT,
country_id INT REFERENCES country(id),
product_category_id INT REFERENCES product_category(id)
)"""

cursor.execute(product)
cursor.close(product)

order = """CREATE TABLE orders(
id SERIAL PRIMARY KEY,
employee_id INT REFERENCES employee(id),
city_id INT REFERENCES city(id),
date_of_order DATE NOT NULL,
customer_id INT REFERENCES customer(id),
product_id INT REFERENCES product(id),
price FLOAT NOT NULL
)"""

cursor.execute(order)
cursor.close(order)


connection.commit()

cursor.close()
connection.close()
