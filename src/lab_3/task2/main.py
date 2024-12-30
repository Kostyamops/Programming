from PIL.ImageChops import duplicate
from scipy.constants import point
from sympy import intervals

from src.lab_3.defs import read_file
from operator import itemgetter


class Person:

    def __init__(self, name, age): # Задание объекта
        self.name = name
        self.age = int(age)
        self.group = None

    def __str__(self):
        # return (self.name + " (" + str(self.age) + ")" + " " + str(self.group))
        return (self.name + " (" + str(self.age) + ")")


def get_intervals(lst):
    duplicated_list = []

    for i in lst:
        duplicated_list.append(i)
        duplicated_list.append(i + 1)

    duplicated_list.insert(0, 0)
    duplicated_list.append(123)
    lst = list(zip(duplicated_list[::2], duplicated_list[1::2]))
    print(lst)
    return lst


def get_group(intervals, value):
    for i, (low, high) in enumerate(intervals, start=0):
        if low <= value <= high:
            print(value, i)
            return i
    return -1


def output(people, intervals):
    group_start = people[0].group
    group_list = []
    for i in range(len(people)):
        if people[i].group == group_start:
            abc = str(people[i])
            group_list.append(abc)
        else:
            if group_list != []:
                start = (str(intervals[group_start][0]) + "-" + str(intervals[group_start][1]) + ": ")
                ending = str(', '.join(map(str, group_list)))
                print(start + ending)
            group_list = [str(people[i])]
            group_start = int(people[i].group)
    if group_list != []:
        start = (str(intervals[group_start][0]) + "-" + str(intervals[group_start][1]) + ": ")
        ending = str(', '.join(map(str, group_list)))
        print(start + ending)


if __name__ == "__main__":
    print("Введите интервалы:")
    intervals = get_intervals(list(map(int, str(input()).split())))

    list1 = read_file("../../../txtf/lab_3/task2/list100.txt")
    people = [Person(f"{list1[i][0]}", f"{list1[i][1]}") for i in range(len(list1))]  # Создаем массив из объектов класса

    for i in range(len(people)):
        # print(f"Object_{i}: ", people[i])
        people[i].group = get_group(intervals, (people[i]).age)

    people.sort(key=lambda Person: (-Person.group, -Person.age, Person.name)) # Сортируем по возрасту в порядке не убывания

    # for i in range(len(people)):
    #     print(f"Object_{i}: ", people[i])

    output(people, intervals)