import io


def read_file(path):
    with io.open(path, "r", encoding='utf-8') as file:
        line = file.readline()
        a = []
        while line != "END":
            a.append([int(x) if x.isdigit() else x for x in (str(line)[:-1]).split(",")])
            line = file.readline()
            # print(line)
    file.close()
    # for i in range(len(a)):
    #     print(a[i])
    return a

def read_file_task1(path):
    with open(path, "r") as file:
        a = []
        line = file.readline()
        while line != "END":
            a.append(list(map(int, line.split(","))))
            line = file.readline()
    file.close()
    return a

def write_file(path, output):
    with open(path, "w") as file:
        for i in output:
            file.write(str(i))
            file.write("\n")
    file.close()