from PIL import Image
import numpy as np


directions = {'top': 0, 'right': 1, 'bottom': 2, 'left': 3}


def generate_ant_path(
    board_size: tuple[int, int],
    init_ant_pos: tuple[int, int],
    direction: str,
    turn_on_first_step: bool = False
) -> tuple[list[list[int]], int, int]:
    """
    #### Функция для нахождения пути муравья\
    от его стартовой точки до границы поля на плоскости.
    - параметр direction может принимать значения: 'top', 'right', 'bottom', 'left'.
    """

    # Размеры поля по которому движется муравей
    width, height = board_size

    # Изначальные координаты муравья
    row, col = init_ant_pos

    # Изначальное направление муравья
    direction = directions[direction]

    # Определяем должен ли муравей повернуться на первом шаге
    if not turn_on_first_step:
        direction = 3 if direction == 0 else direction - 1

    # Создаем 2D матрицу размером width X height,
    # заполненную числом 255 (белый цвет в RGB системе)
    matrix = [[255] * width for _ in range(height)]

    # Счетчик шагов муравья
    steps = 0
    # Счетчик черных клеток
    black_cells = 0

    # Выполняем цикл пока муравей не дойдет до любой из границ поля
    while 0 <= row < width and 0 <= col < height:

        if matrix[row][col] == 255:
            # если клетка белая - муравей поворачиваеться вправо
            direction = (direction + 1) % 4
            # инвертируем цвет текущей клетки на противоположный
            # и изменяем счетчик количества черных клеток
            matrix[row][col] = 0
            black_cells += 1
        else:
            # если клетка черная - муравей поворачиваеться влево
            direction = (direction - 1) % 4
            matrix[row][col] = 255
            black_cells -= 1

        # Перемещаем муравья в сторону в которую он направлен
        match direction:
            case 0: row -= 1
            case 1: col += 1
            case 2: row += 1
            case 3: col -= 1

        # Увеличиваем счетчик шагов на один шаг
        steps += 1

        # Для отладки
        # print(f"Шаг: {steps}\nМатрица:\n{np.asarray([*matrix], np.dtype('uint8'))}\n")

    return matrix, steps, black_cells


def main():
    board_size = (1024, 1024)
    init_ant_pos = (512, 512)
    direction = 'top'
    turn_on_first_step = True

    ant_path_2d_list, steps_taken, black_cells = generate_ant_path(
        board_size, init_ant_pos, direction, turn_on_first_step
    )

    ant_path_2d_array = np.asarray([*ant_path_2d_list], np.dtype('uint8'))

    print(f'Количество шагов затраченных для достижение границы поля:\n{steps_taken}')
    print(f'Количество черных клеток когда муравей дошел до границы поля:\n{black_cells}')
    print(f'Результирующая матрица:\n{ant_path_2d_array}')

    img = Image.fromarray(ant_path_2d_array, 'L').convert('1')
    img.save(
        f'antpath_black-cells{black_cells}_board{"x".join(map(str, board_size))}'
        f'_antpos{"x".join(map(str, init_ant_pos))}'
        f'_direct-{direction}'
        f'_turn-{turn_on_first_step}.png'.lower()
    )


if __name__ == '__main__':
    main()
