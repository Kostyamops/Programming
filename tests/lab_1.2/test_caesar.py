import unittest

from src.lab_2.caesar import encrypt_caesar, decrypt_caesar


class CaesarTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_encrypt(self):
        self.assertEquals(encrypt_caesar("Python 3.6", 2), "Ravjqp 3.6")
        self.assertEquals(encrypt_caesar("1@#&*^6", 16), "1@#&*^6")
        self.assertEquals(encrypt_caesar("Hello World!", 3), "Khoor Zruog!")


    def test_decrypt(self):
        self.assertEquals(decrypt_caesar("Ravjqp 3.6", 2), "Python 3.6")
        self.assertEquals(decrypt_caesar("MXQS Yrmzivwmxc", 4), "ITMO University")
        self.assertEquals(decrypt_caesar("AjmzIQ", 8), "SberAI")