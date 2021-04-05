def f(x):
    return x ** 2


a = [1, 2, 7, 9, 100]

b = list(map(f, a))
print(b)


def is_odd(x):
    return x % 2 != 0


c = list(filter(is_odd, a))
print(c)


# def is_prime(n):
#     for d in range(2, n):
#         if n % d == 0:
#             return False
#     else:
#         return True


def is_prime(n):
    return all(n % d != 0 for d in range(2, n))


primes = list(filter(is_prime, range(2, 25)))
print(primes)
