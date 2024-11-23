import string
import unittest
import random

from src.lab_2.vigenere import encrypt_vigenere, decrypt_vigenere


class VigenereTestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_encrypt(self):
        self.assertEquals(encrypt_vigenere("Python 3.6", "language"), "Aygnin 3.6")
        self.assertEquals(encrypt_vigenere("PYTHON", "CODE"), "RMWLQB")
        self.assertEquals(encrypt_vigenere("Meine freunde", "Deutsch"), "Picgw muiogvg")
        self.assertEquals(encrypt_vigenere("1@#&*^6", "None"), "1@#&*^6")


    def test_decrypt(self):
        self.assertEquals(decrypt_vigenere("Aygnin 3.6", "language"), "Python 3.6")
        self.assertEquals(decrypt_vigenere("Sfpipt 777", "abc"), "Senior 777")
        self.assertEquals(decrypt_vigenere("LhzAcseew", "SaveYourTears"), "TheWeeknd")

    def test_randomized(self):
        kwlen = random.randint(4, 24)
        keyword = ''.join(random.choice(string.ascii_letters) for _ in range(kwlen))
        plaintext = ''.join(random.choice(string.ascii_letters + ' -,') for _ in range(64))
        ciphertext = encrypt_vigenere(plaintext, keyword)
        self.assertEqual(plaintext, decrypt_vigenere(ciphertext, keyword))