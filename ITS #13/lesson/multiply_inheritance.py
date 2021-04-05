"""
Множественные наследование
"""
from time import sleep


class MyTime:

    def __init__(self, h=0, m=0, s=0):
        self.hours = h
        self.minutes = m
        self.seconds = s

    def __str__(self):
        return f'{self.hours:0>2d}:{self.minutes:0>2d}:{self.seconds:0>2d}'

    def tick(self):
        self.seconds += 1
        self.minutes += self.seconds // 60
        self.seconds %= 60
        self.hours += self.minutes // 60
        self.minutes %= 60
        self.hours %= 24


class MyDate:

    def __init__(self, day=1, month=1, year=2021):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f'{self.day:0>2d}.{self.month:0>2d}.{self.year:0>4d}'

    def next_day(self):
        if (self.day == 28 and self.month == 2) \
                or (self.day == 30 and self.month in [4, 6, 9, 11]) \
                or (self.day == 31 and self.month in [1, 3, 5, 8, 10, 12]):
            self.day = 1
            self.next_month()
        else:
            self.day += 1

    def next_month(self):
        if self.month == 12:
            self.month = 1
            self.next_year()
        else:
            self.month += 1

    def next_year(self):
        self.year += 1


class MyTimeDate(MyTime, MyDate):
    def __init__(self, day=1, month=1, year=2021, hours=0, minutes=0, seconds=0):
        MyTime.__init__(self, hours, minutes, seconds)
        MyDate.__init__(self, day, month, year)

    def __str__(self):
        return f'{MyDate.__str__(self)} ~ {MyTime.__str__(self)}'

    def tick(self):
        MyTime.tick(self)
        if self.hours == 0 and self.minutes == 0 and self.seconds == 0:
            MyDate.next_day(self)


if __name__ == '__main__':
    # d1 = MyDate(25, 12)
    # for _ in range(10):
    #     d1.next_day()
    #     print(d1)
    #
    # t1 = MyTime(23, 59, 55)
    # for _ in range(10):
    #     t1.tick()
    #     print(t1)

    my_datetime = MyTimeDate(31, 12, 2021, 23, 59, 58)
    for i in range(15555555550):
        sleep(0.98)
        my_datetime.tick()
        print(my_datetime)
