import unittest

from src.lab_3.task1.main import duplicates_remove, get_recommendation


class RSATestCase(unittest.TestCase):

    # Тест для проверки работы, можно удалить
    def test_duplicates_remove(self):
        self.assertEquals(duplicates_remove([[1, 2, 2], [2, 2, 2], [2, 3, 3, 3, 4]]), [[1, 2], [2], [2, 3, 4]])
        self.assertEquals(duplicates_remove([[2, 3, 4]]), [[2, 3, 4]])
        self.assertEquals(duplicates_remove([[1, 1, 2, 2, 3], []]), [[1, 2, 3], []])

    def test_get_recommendation(self):
        self.assertEquals(get_recommendation([[1, 2.68], [2, 27.1], [3, 11], [4, 0]]),2)
        self.assertEquals(get_recommendation([[1, 0], [2, 0], [3, 0], [4, 0], [5, 1]]), 5)
        self.assertEquals(get_recommendation([[7, 1234432], [2, -1893], [123, 112], [13, 1]]), 7)