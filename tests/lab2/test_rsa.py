import unittest

from src.lab2.rsa import is_prime, gcd, extended_gcd, multiplicative_inverse


class RSATestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_isprime(self):
        self.assertEquals(is_prime(11), True)
        self.assertEquals(is_prime(9973), True)
        self.assertEquals(is_prime(24680), False)
        self.assertEquals(is_prime(1), False)

    def test_gcd(self):
        self.assertEquals(gcd(12, 15), 3)
        self.assertEquals(gcd(11,121), 11)
        self.assertEquals(gcd(7, 8963), 1)
        self.assertEquals(gcd(7, 3), 1)