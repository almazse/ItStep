from math import sqrt
import doctest
# функция расчета гипотенузы
def hipotenuse(a: float, b: float) -> float:
    """
    Returns the value of hipotenuse of right triangle
    Args:
        a (float): first cathetus
        b (float): second cathetus

    For example:
    >>> hipotenuse(5, 12)
    13.0
    >>> hipotenuse(40, 30)
    50.0
    """
    return sqrt(a ** 2 + b ** 2)


if __name__ == '__main__':
    help(hipotenuse)
    doctest.testmod()
    a = 3.0
    b = 4.0
    print(f'S = {hipotenuse(a, b):.3f}')
