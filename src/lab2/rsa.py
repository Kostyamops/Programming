import random

def is_prime(n: int) -> bool:
    """
    >>> is_prime(2)
    True
    >>> is_prime(11)
    True
    >>> is_prime(8)
    False
    """
    if n == 1:
        return False
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


def generate_keypair(p: int, q: int) -> tuple[tuple[int, int], tuple[int, int]]:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Числа дожны быть простыми.')
    elif p == q:
        raise ValueError('p и q не могут быть равными.')

    n = p*q

    phi = (p-1)*(q-1)

    #Выбираем e
    e = random.randrange(1, phi)
    g = gcd(e, phi)

    #Проверяем что e и phi взаимно простые
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))


def gcd(a: int, b: int) -> int:
    """
    >>> gcd(12, 15)
    3
    >>> gcd(3, 7)
    1
    """
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a + b)


def multiplicative_inverse(e: int, phi: int) -> int:
    """
    >>> multiplicative_inverse(7, 40)
    23
    """

    gcd, x, y = extended_gcd(e, phi)
    if gcd == 1:
        return x % phi
    raise ValueError("Inverse don't exist")

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x