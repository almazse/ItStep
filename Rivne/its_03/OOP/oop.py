from person import Person
from house import *

person1 = Person('Bob', 35)
person2 = Person('Kate', 30)

house1 = House('Street 1')
house1.settle(person1)
house1.settle(person2)

person1.description_of_person()
person2.description_of_person()

house1.show_residents()