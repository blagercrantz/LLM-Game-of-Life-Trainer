import random

grid_side_length = 3
grid = []
grid_2 = []

def create_grid():
    global grid, grid_2
    grid = []
    for _ in range(grid_side_length):
        row = []
        row_2 = []
        for _ in range(grid_side_length):
            if random.randint(1, 3) == 1:
                row.append(1)
            else:
                row.append(0)
            row_2.append(0)
        grid.append(row)
        grid_2.append(row_2)

def check():
    global grid_2
    for i in range(grid_side_length):
        for j in range(grid_side_length):
            for l in range(-1, 2):
                for m in range(-1, 2):
                    if not (l == 0 and m == 0):
                        if i + l >= 0 and i + l < grid_side_length and j + m >= 0 and j + m < grid_side_length:
                            if grid[i + l][j + m] == 1:
                                grid_2[i][j] += 1

def iterate():
    global grid
    for i in range(grid_side_length):
        for j in range(grid_side_length):
            if grid[i][j] == 0:
                if grid_2[i][j] == 3:
                    grid[i][j] = 1
            else:
                if grid_2[i][j] < 2 or grid_2[i][j] > 3:
                    grid[i][j] = 0
create_grid()

print(f'''The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbors, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

Here is a {grid_side_length}x{grid_side_length} grid of square cells; 0 marks a dead cell and 1 marks a live cell:
''')
      
for row in grid:
    print(' '.join(map(str, row)))
      
print('''
What will the grid look like after one step in time?

Correct answer:
''')

check()
iterate()

for row in grid:
    print(' '.join(map(str, row)))
