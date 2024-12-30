from sympy.physics.units import percent

from src.lab_3.defs import read_file, read_file_task1


class Movie:

    def __init__(self, name):  # Задание объекта
        self.name = name
        self.views = 0
        self.users_rate = 0
        self.in_recommendations = True

    def __str__(self):
        return (self.name)


def get_recommendation(data):
    # output = (list1[sorted(data, reverse=True, key=lambda x: x[1])[0][0]-1][1])
    output = (sorted(data, reverse=True, key=lambda x: x[1])[0][0])
    return output



def duplicates_remove(a):
    b = []
    for i in a:
        unique_subarray = list(dict.fromkeys(i))
        b.append(unique_subarray)
    return b


if __name__ == "__main__":
    print("Введите историю просмотра пользователя:")
    user_history = sorted(list(map(int, str(input()).split(","))))
    # print(*user_history)

    # user_history = [2, 4]

    list1 = read_file("../../../txtf/lab_3/task1/movies20.txt")
    movies = [Movie(f"{list1[i]}") for i in range(0, len(list1))]  # Создаем массив из объектов класса
    # print(*movies)

    users = sorted(read_file_task1("../../../txtf/lab_3/task1/history_generated.txt"))

    for i in users:
        for j in range(len(i)):
            # print(i[j]-1)
            movies[i[j]-1].views += 1
            if i[j] in user_history:
                movies[i[j]-1].in_recommendations = False

    users = duplicates_remove(users) # Убираем дубликаты
    user_history = list(set(user_history))

    for i in users:
        percent = 0
        for j in range(len(i)):
            # print("Если " + str(i[j]) + " в " + str(user_history) + ", то percent += 1")
            if i[j] in user_history:
                percent += 1
        percent = round(percent/len(i), 2)
        # print(percent)
        if percent >= 0.5:
            for j in range(len(i)):
                movies[i[j]-1].users_rate += (percent * int(movies[i[j]-1].views))

    recommendation_list = []
    for i in range(len(movies)):
        print(f"Просмотры {i+1}:", movies[i].views, f" Рекомендуется:", movies[i].in_recommendations, f" Рекомендуется:", movies[i].users_rate)
        if movies[i].in_recommendations == True and movies[i].users_rate != 0:
            recommendation_list.append([i+1, movies[i].users_rate])
    # print(recommendation_list)

    if recommendation_list != []:
        output = list1[get_recommendation(recommendation_list)-1][1]
        print(output)
    else:
        print("У нас слишком мало информации о вас для формирования рекомендаций")