import unittest

from src.lab_3.task2.main import get_intervals, get_group


class RSATestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_get_intervals(self):
        self.assertEquals(get_intervals([18, 25, 35, 45, 60, 80, 100]), [(0, 18), (19, 25), (26, 35), (36 ,45), (46, 60), (61, 80), (81, 100), (101, 123)])
        self.assertEquals(get_intervals([1, 18, 24]), [(0, 1), (2, 18), (19, 24), (25, 123)])
        self.assertEquals(get_intervals([18, 25]), [(0, 18), (19, 25), (26, 123)])
        self.assertEquals(get_intervals([1, 2, 3, 4]), [(0, 1), (2, 2), (3, 3), (4, 4), (5, 123)])

    def test_get_group(self):
        self.assertEquals(get_group([(0, 18), (19, 25), (26, 35), (36, 45), (46, 60), (61, 80), (81, 100), (101, 123)], 26),2)
        self.assertEquals(get_group([(0, 1), (2, 18), (19, 24), (25, 123)], 0), 0)
        self.assertEquals(get_group([(0, 18), (19, 25), (26, 123)], 124), -1)
        self.assertEquals(get_group([(0, 1), (2, 2), (3, 3), (4, 4), (5, 123)], 72), 4)