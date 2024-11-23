import random

print("Введите число пользователей:")
users = int(input())
print("Введите число фильмов:")
movies = int(input())
print("Введите максимально возможное число просмотренных фильмов:")
movies_max = int(input())

with open("history_generated.txt", "w") as file:
    output = []
    for i in range(0, users):
        line = ""
        for j in range(0, random.randint(1, movies_max+1)):
            line += str(random.randint(1, movies+1) + ",")
        file.write(line[:-1]+"\n")
    file.write("END")
file.close()