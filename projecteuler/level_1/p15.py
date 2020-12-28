def lattice_paths(grid_size: int) -> int:
    grid = [[2 for _ in range(grid_size)] for _ in range(grid_size)]

    for i in range(1, grid_size):
        grid[0][i] = grid[0][i - 1] + 1
        grid[i][0] = grid[i - 1][0] + 1

    for x in range(1, grid_size):
        for y in range(1, grid_size):
            grid[x][y] = grid[x - 1][y] + grid[x][y - 1]

    return grid[-1][-1]

if __name__ == "__main__":
    print(lattice_paths(20))
