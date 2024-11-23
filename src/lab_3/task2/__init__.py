from src.lab_3.task2.main import get_intervals, Person, get_group, output
from src.lab_3.defs import read_file


if __name__ == "__main__":
    print("Введите интервалы:")

    # 18 25 35 45 60 80 100

    intervals = get_intervals(list(map(int, str(input()).split())))

    list1 = read_file("../../../txtf/lab_3/task2/list100.txt")
    people = [Person(f"{list1[i][0]}", f"{list1[i][1]}") for i in range(len(list1))]  # Создаем массив из объектов класса

    for i in range(len(people)):
        people[i].group = get_group(intervals, (people[i]).age)

    people.sort(key=lambda Person: (-Person.group, -Person.age, Person.name)) # Сортируем по возрасту в порядке не убывания

    # for i in range(len(people)): # Вывод всех объектов
    #     print(f"Object_{i}: ", people[i])

    output(people, intervals)