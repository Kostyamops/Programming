import multiprocessing
import pathlib
import random
import time
import typing as tp

T = tp.TypeVar("T")


def read(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """Прочитать Судоку из указанного файла"""
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку"""
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов

    >>> group([1,2,3,4], 2)
    [[1, 2], [3, 4]]
    >>> group([1,2,3,4,5,6,7,8,9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    return [values[i : i + n] for i in range(0, len(values), n)]


def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos

    >>> get_row([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '2', '.']
    >>> get_row([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (1, 0))
    ['4', '.', '6']
    >>> get_row([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (2, 0))
    ['.', '8', '9']
    """
    row, col = pos  # Получаем номер строки и столбца из позиции
    return grid[row]  # Возвращаем строку


def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos

    >>> get_col([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']], (0, 0))
    ['1', '4', '7']
    >>> get_col([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']], (0, 1))
    ['2', '.', '8']
    >>> get_col([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']], (0, 2))
    ['3', '6', '9']
    """
    row, col = pos  # Получаем номер строки и столбца из позиции
    return [grid[i][col] for i in range(len(grid))]  # Возвращаем столбец


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos

    >>> grid = read_sudoku('puzzle1.txt')
    >>> get_block(grid, (0, 1))
    ['5', '3', '.', '6', '.', '.', '.', '9', '8']
    >>> get_block(grid, (4, 7))
    ['.', '.', '3', '.', '.', '1', '.', '.', '6']
    >>> get_block(grid, (8, 8))
    ['2', '8', '.', '.', '.', '5', '.', '7', '9']
    """
    row, col = pos  # Получаем номер строки и столбца из позиции
    block_row = (row // 3) * 3  # Находим верхнюю границу блока по строкам
    block_col = (col // 3) * 3  # Находим левую границу блока по столбцам
    return [
        grid[r][c]
        for r in range(block_row, block_row + 3)  # Возвращаем все значения в блоке 3x3
        for c in range(block_col, block_col + 3)
    ]


def find_empty_positions(
    grid: tp.List[tp.List[str]],
) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле

    >>> find_empty_positions([['1', '2', '.'], ['4', '5', '6'], ['7', '8', '9']])
    (0, 2)
    >>> find_empty_positions([['1', '2', '3'], ['4', '.', '6'], ['7', '8', '9']])
    (1, 1)
    >>> find_empty_positions([['1', '2', '3'], ['4', '5', '6'], ['.', '8', '9']])
    (2, 0)
    """
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == ".":
                return row, col  # Возвращаем координаты пустой позиции
    return None  # Если пустых позиций нет, возвращаем None


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции

    >>> grid = read_sudoku('puzzle1.txt')
    >>> values = find_possible_values(grid, (0,2))
    >>> values == {'1', '2', '4'}
    True
    >>> values = find_possible_values(grid, (4,7))
    >>> values == {'2', '5', '9'}
    True
    """
    possible_values = set("123456789")  # Все возможные значения от 1 до 9

    # Получаем значения из строки, столбца и блока
    row_values = set(get_row(grid, pos))
    col_values = set(get_col(grid, pos))
    block_values = set(get_block(grid, pos))

    # Убираем уже существующие значения
    return possible_values - row_values - col_values - block_values


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """Решение пазла, заданного в grid"""
    """ Как решать Судоку?
        1. Найти свободную позицию
        2. Найти все возможные значения, которые могут находиться на этой позиции
        3. Для каждого возможного значения:
            3.1. Поместить это значение на эту позицию
            3.2. Продолжить решать оставшуюся часть пазла

    >>> grid = read_sudoku('puzzle1.txt')
    >>> solve(grid)
    [['5', '3', '4', '6', '7', '8', '9', '1', '2'], ['6', '7', '2', '1', '9', '5', '3', '4', '8'], ['1', '9', '8', '3', '4', '2', '5', '6', '7'], ['8', '5', '9', '7', '6', '1', '4', '2', '3'], ['4', '2', '6', '8', '5', '3', '7', '9', '1'], ['7', '1', '3', '9', '2', '4', '8', '5', '6'], ['9', '6', '1', '5', '3', '7', '2', '8', '4'], ['2', '8', '7', '4', '1', '9', '6', '3', '5'], ['3', '4', '5', '2', '8', '6', '1', '7', '9']]
    """
    # Находим пустую позицию
    empty_pos = find_empty_positions(grid)

    # Если пустых позиций нет, возвращаем заполненную сетку
    if not empty_pos:
        return grid

    # Находим возможные значения для найденной пустой позиции
    possible_values = find_possible_values(grid, empty_pos)

    row, col = empty_pos  # Получаем координаты пустой позиции

    for value in possible_values:
        grid[row][col] = value  # Пробуем заполнить позицию одним из возможных значений

        # Рекурсивно пытаемся решить оставшуюся часть Судоку
        if solve(grid):
            return grid

        # Если решение не удалось, откатываем изменения
        grid[row][col] = "."

    return None  # Если нет решений, возвращаем None


def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """Если решение solution верно, то вернуть True, в противном случае False"""

    square_len = 9

    def check_block(block: tp.List[str]) -> bool:
        """Проверяет, что блок содержит все числа от 1 до 9 без повторений"""
        block = [num for num in block if num != "."]
        return len(block) == len(set(block)) and set(block) == set("123456789")

    # Проверяем каждую строку
    for row in solution:
        if not check_block(row):
            return False

    # Проверяем каждый столбец
    for col_idx in range(square_len):
        col = [solution[row_idx][col_idx] for row_idx in range(square_len)]
        if not check_block(col):
            return False

    # Проверяем каждый блок 3x3
    for block_row in range(0, square_len, 3):
        for block_col in range(0, square_len, 3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(solution[block_row + i][block_col + j])
            if not check_block(block):
                return False

    return True  # Если все проверки пройдены, возвращаем True


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов

    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    cells_count = 81
    square_len = 9
    # Инициализируем пустую сетку Судоку
    grid = [["." for _ in range(square_len)] for _ in range(square_len)]

    # Заполняем сетку Судоку
    solve(grid)

    # Получаем все возможные позиции для заполнения
    filled_positions = [(i, j) for i in range(square_len) for j in range(square_len)]

    # Перемешиваем позиции для случайного удаления значений
    random.shuffle(filled_positions)

    # Удаляем элементы, чтобы оставить только N заполненными
    for i in range(cells_count - N):
        row, col = filled_positions[i]
        grid[row][col] = "."

    return grid  # Возвращаем сгенерированную сетку Судоку


def run_solve(fname):
    grid = read(fname)
    start = time.time()
    solve(grid)
    end = time.time()
    print(f"{fname}: {end - start}")


if __name__ == "__main__":
    for fname in ("puzzle1.txt"):
        p = multiprocessing.Process(target=run_solve, args=(fname,))
        p.start()