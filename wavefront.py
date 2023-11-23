import numpy as np


def wavefront(grid, start, goal):
    rows, cols = grid.shape
    wavefront_map = np.zeros_like(grid, dtype=int)

    # Definir o ponto de destino
    goal_x, goal_y = goal
    wavefront_map[goal_x, goal_y] = 1

    # Propagar ondas
    wave_number = 1
    while wavefront_map[start] == 0:
        for i in range(rows):
            for j in range(cols):
                if grid[i, j] == 0 and wavefront_map[i, j] == wave_number:
                    vizinhos = [
                        (i - 1, j),
                        (i + 1, j),
                        (i, j - 1),
                        (i, j + 1),
                        (i - 1, j - 1),
                        (i - 1, j + 1),
                        (i + 1, j - 1),
                        (i + 1, j + 1),
                    ]

                    for x, y in vizinhos:
                        if (
                            0 <= x < rows
                            and 0 <= y < cols
                            and grid[x, y] == 0
                            and wavefront_map[x, y] == 0
                        ):
                            wavefront_map[x, y] = wave_number + 1

        wave_number += 1

    return wavefront_map


def print_wavefront_map(wavefront_map):
    rows, cols = wavefront_map.shape
    for i in range(rows):
        for j in range(cols):
            print(f"{wavefront_map[i, j]:2}", end=" ")
        print()


def main():
    # Definir um grid 2D (0 = espaço livre, 1 = obstáculo)
    grid = np.array(
        [
            [0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
    )

    # Ponto de origem
    start = (0, 0)

    # Ponto de destino
    goal = (4, 4)

    wavefront_map = wavefront(grid, start, goal)

    print("Mapa de Wavefront:")
    print_wavefront_map(wavefront_map)


if __name__ == "__main__":
    main()
