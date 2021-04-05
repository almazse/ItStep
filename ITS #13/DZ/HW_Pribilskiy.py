class Car:
    def __init__(self, model, year, manufacturer, engine_displacement, color, price):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_displacement = engine_displacement
        self.__color = color
        self.__price = price

    def buy_cars(self):
        return f'Congratulations good choice. {self.__manufacturer} {self.__model} ({self.__year}): color: {self.__color}, ' \
               f'engine: {self.__engine_displacement}l, {self.__price}$'

    def change_settings(self, engine, color):
        self.__engine_displacement = engine
        self.__color = color

    def get_year(self):
        return f'This car is a {self.__year} model year'


class Book:
    def __init__(self, title, year, publisher, genre, author, price):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def __getattr__(self, attr):
        try:
            return f'{self.attr}'
        finally:
            return 'None attribute'

    def change_price(self, value):
        if type(value) == int:
            self.price = value
        else:
            print('the price must be an integer')

    def get_upper_title(self):
        return self.title.upper()


class Stadium(Book):
    def __init__(self, title, opening_date, country, city, capacity):
        super().__init__(title, year=0, publisher=0, genre=0, author=0, price=0)
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def __str__(self):
        return f"{self.get_upper_title()}, {self.opening_date}, {self.country}, {self.city}, {self.capacity}"


if __name__ == '__main__':
    bmw = Car('X3', 2019, 'BMW', 3.5, 'black', 25000)
    bmw.change_settings(4.0, 'silver')
    print(bmw.buy_cars())
    print(bmw.get_year())

    print()

    HarryPotter = Book("Harry Potter", 2020, "Bloomsbury", "Fantastic", "J. K. Rowling", 30)
    print(HarryPotter.title)
    print(HarryPotter.title1)

    print(f'Price = {HarryPotter.price}')
    HarryPotter.change_price(20)
    print(f'Price = {HarryPotter.price}')
    print(HarryPotter.get_upper_title())

    print()
    barcelona = Stadium("Camp Nou", "24.09.1957", "Spain", "Barcelona", 99354)
    cairo = Stadium("Cairo International Stadium", "23.06.1960", "Egypt", "Cairo", 73000)
    madrid = Stadium("Estadio Santiago Bernabéu", "14.12.1947", "Spain", "Madrid", 	81044)

    print(barcelona, "\n", cairo, "\n", madrid)
