import unittest
from src.lab_4.defs import *


class RSATestCase(unittest.TestCase):

    def test_check_id(self):
        self.assertEqual(
            check_id('12345'),
            True)
        self.assertEqual(
            check_id('21553423243462'),
            False)
        self.assertEqual(
            check_id('iiuhd'),
            False)
        self.assertEqual(
            check_id('no data'),
            False)

    def test_get_cart_dict(self):
        self.assertEqual(
            get_cart_dict("Чай, Чай, Чай, Чай, Чай"),
            {"Чай": 5})
        self.assertEqual(
            get_cart_dict("Сосиски, Колбаса, Кофе"),
            {"Сосиски": 1, "Колбаса": 1, "Кофе": 1})
        self.assertEqual(
            get_cart_dict("Картофель"),
            {"Картофель": 1})
        self.assertEqual(
            get_cart_dict("Колбаса, Кофе, Чай, Чай, Чай, Кофе"),
            {"Колбаса": 1, "Кофе": 2, "Чай": 3})

    def test_get_cart_list(self):
        self.assertEqual(
            get_cart_list({"Чай": 5}),
            "Чай x5")
        self.assertEqual(
            get_cart_list({"Сосиски": 1, "Колбаса": 1, "Кофе": 1}),
            "Сосиски, Колбаса, Кофе")
        self.assertEqual(
            get_cart_list({"Картофель": 1}),
            "Картофель")
        self.assertEqual(
            get_cart_list({"Колбаса": 1, "Кофе": 2, "Чай": 3}),
            "Колбаса, Кофе x2, Чай x3")

    def test_check_name(self):
        self.assertEqual(
            check_name("Белова Екатерина Михайловна"),
            True)
        self.assertEqual(
            check_name("Николаев Николай"),
            True)
        self.assertEqual(
            check_name(""),
            False)
        self.assertEqual(
            check_name("Иван"),
            False)

    def test_check_address(self):
        self.assertEqual(
            check_address("Великобритания. Англия. Лондон. Бейкер-стрит"),
            True)
        self.assertEqual(
            check_address("Россия. Ленинградская область. Санкт-Петербург. набережная реки Фонтанки"),
            True)
        self.assertEqual(
            check_address("Япония. Шибуя. Шибуя-кроссинг"),
            False)
        self.assertEqual(
            check_address("no data"),
            False)

    def test_check_number(self):
        self.assertEqual(
            check_number('+3-061-234-56-78'),
            True)
        self.assertEqual(
            check_number('+7-912-345-67-89'),
            True)
        self.assertEqual(
            check_number('+34-93-1234-567'),
            False)
        self.assertEqual(
            check_number('no data'),
            False)

    def test_check_priority(self):
        self.assertEqual(
            check_priority("MAX"),
            True)
        self.assertEqual(
            check_priority("MIDDLE"),
            True)
        self.assertEqual(
            check_priority("LOW"),
            True)
        self.assertEqual(
            check_priority("no data"),
            False)

    def test_error_message(self):
        self.assertEqual(error_message(
            ['90385', 'Макароны, Сыр, Макароны, Сыр', 'Николаев Николай', 'no data', '+1-416-123-45-67', 'LOW'], 1),
            "90385;1;no data")
        self.assertEqual(error_message(
            ['65829', 'Сок, Вода, Сок, Вода', 'Белова Екатерина Михайловна', 'Испания. Каталония. Барселона. Рамбла', '+34-93-1234-567', 'LOW'], 2),
            "65829;2;+34-93-1234-567")
        self.assertEqual(error_message(
            ['84756', 'Печенье, Сыр, Печенье, Сыр', 'Васильева Анна Владимировна', 'Япония. Шибуя. Шибуя-кроссинг', '+8-131-234-5678', 'MAX'], 3),
            "84756;1;Япония. Шибуя. Шибуя-кроссинг\n84756;2;+8-131-234-5678")

    def test_fix(self):
        self.assertEqual(
            fix(['90385', 'Макароны, Сыр, Макароны, Сыр', 'Николаев Николай', '', '+1-416-123-45-67', 'LOW']),
            ['90385', 'Макароны, Сыр, Макароны, Сыр', 'Николаев Николай', 'no data', '+1-416-123-45-67', 'LOW'])
        self.assertEqual(
            fix(["", "", "", "", "", ""]),
            ["no data", "no data", "no data", "no data", "no data", "no data"])
        self.assertEqual(
            fix([""]),
            ["no data"])

    def test_check_valid(self):
        self.assertEqual(
            check_valid(
                ['90385', 'Макароны, Сыр, Макароны, Сыр', 'Николаев Николай', 'no data', '+1-416-123-45-67', 'LOW']),
            (False, 1)
        )
        self.assertEqual(
            check_valid(
                ['65829', 'Сок, Вода, Сок, Вода', 'Белова Екатерина Михайловна', 'Испания. Каталония. Барселона. Рамбла', '+34-93-1234-567', 'LOW']),
            (False, 2)
        )
        self.assertEqual(
            check_valid(['84756', 'Печенье, Сыр, Печенье, Сыр', 'Васильева Анна Владимировна', 'Япония. Шибуя. Шибуя-кроссинг', '+8-131-234-5678', 'MAX']),
            (False, 3)
        )
        self.assertEqual(
            check_valid(['72901', 'Чай, Кофе, Чай, Кофе', 'Михайлов Сергей Петрович', 'Великобритания. Англия. Лондон. Бейкер-стрит', '+4-207-946-09-58', 'LOW']),
            (True, 0)
        )