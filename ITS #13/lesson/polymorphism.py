class Student:
    id = 0

    def __init__(self, name):
        self.name = name
        Student.id += 1
        self.id = Student.id

    def speak(self):
        print(f'Hi, i\'m students {self.name}, '
              f'my id ={self.id}')

    def __str__(self):
        return f'Student #{self.id} ~ {self.name}'


class Aspirant(Student):
    def __init__(self, name):
        Student.__init__(self, name)

    def speak(self):
        print(f'Hi, i\'m aspirant {self.name}, '
              f'my id ={self.id}')

    def say_hi(self):
        print(f'{self.name} say HI')


if __name__ == '__main__':
    names = ['John', 'Bella', 'Vasya', 'Maria', 'Elizaveta']
    students = []
    for i in range(len(names)):
        if i % 2 == 0:
            students.append(Student(names[i]))
        else:
            students.append(Aspirant(names[i]))

    [(print(isinstance(student, Student), print(student))) for student in students]

    [student.say_hi() for student in students if isinstance(student, Aspirant)]
    [student.speak() for student in students]