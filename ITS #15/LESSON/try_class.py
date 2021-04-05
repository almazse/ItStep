# class NewBow(object):
#     def __init__(self, name, surname):
#         self._name = name
#         self._surname = surname
#
#
# class NewInt(int):
#     pass

DATA = [(2, 3), (5, 2), (12, 5), (2, 8), (27, 9), (1, 6)]


class Fraction:
    def __init__(self, numerator, denominator):
        self._numerator = numerator
        self._denominator = denominator

    def __str__(self):
        if self._numerator == 0:
            return '0'
        if self._numerator % self._denominator == 0:
            return f'{self._numerator}'
        if self._numerator > self._denominator:
            int_part = self._numerator // self._denominator
            fract_part = self._numerator - int_part * self._denominator
            return f'{int_part} {fract_part}/{self._denominator}'
        return f'{self._numerator}/{self._denominator}'

    def __float__(self):
        return self._numerator / self._denominator

    def __eq__(self, other):
        return float(self) == float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __add__(self, other):
        a, b, c, d = self._numerator, self._denominator, other._numerator, other._denominator
        return Fraction(a * d + b * c, b * d)

    def __sub__(self, other):
        a, b, c, d = self._numerator, self._denominator, other._numerator, other._denominator
        return Fraction(a * d - b * c, b * d)

    def __mul__(self, other):
        a, b, c, d = self._numerator, self._denominator, other._numerator, other._denominator
        return Fraction(a * c, b * d)

    def __truediv__(self, other):
        a, b, c, d = self._numerator, self._denominator, other._numerator, other._denominator
        return Fraction(a * d, b * c)

    def __pow__(self, power, modulo=None):
        return Fraction(self._numerator ** power, self._denominator ** power)


if __name__ == '__main__':
    # new_boy_misha = NewBow('Misha', 'Pupkin')
    # print(new_boy_misha.__dict__)
    # print(type(2))
    fractions = [Fraction(*item) for item in DATA]
    for f in fractions:
        print(f)
    print(fractions[0] == fractions[-1])
    print(fractions[0] > fractions[-1])
    print(fractions[0] + fractions[-1])
    print(fractions[0] - fractions[-1])
    print(fractions[0] * fractions[-1])
    print(fractions[0] / fractions[-1])
    print(fractions[0] ** 2)
