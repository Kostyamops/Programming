from sympy.physics.units import percent

from src.lab_3.defs import read_file


class Movie:

    def __init__(self, name):  # Задание объекта
        self.name = name
        self.views = 0
        self.users_rate = 0
        self.in_recommendations = True

    def __str__(self):
        return (self.name)


# class Person:
#
#     def __init__(self, movies, percent): # Задание объекта
#         self.movies_all = list(movies)
#         self.percent = percent
#         self.movies_new = "12345"
#         self.in_recommendations = False
#
#
#     def __str__(self):
#         # return (self.name + " (" + str(self.age) + ")" + " " + str(self.group))
#         return (str(self.movies_all) + " " + str(self.percent) + " " + str(self.in_recommendations))


def get_recommendation():
    return 0


if __name__ == "__main__":
    # print("Введите историю просмотра пользователя:")
    # user_history = sorted(list(map(int, str(input()).split(","))))
    # print(*user_history)

    user_history = [2, 4]

    list1 = read_file("../../../txtf/lab_3/task1/movies_example.txt")
    movies = [Movie(f"{list1[i]}") for i in range(len(list1))]  # Создаем массив из объектов класса
    print(*list1)

    list2 = sorted(read_file("../../../txtf/lab_3/task1/history_example.txt"))
    print(*list2)
    # people = [Person(f"{sorted(list2[i])}", 0.0) for i in range(len(list2))]  # Создаем массив из объектов класса

    # for i in range(len(people)):
    #     percent = 0
    #     for j in range(len(user_history)):
    #         if int(user_history[j]) in people[i].movies_all:
    #             percent += 1
    #             print("OK")
    #         print(user_history[j], people[i].movies_all)
    #     percent = round(percent/len(user_history), 3)
    #     if percent >= 0.5:
    #         people[i].in_recommendations = True
    #     people[i].percent = percent
    
    for i in range(len(movies)):
        print(f"Object_{i}: ", movies[i])