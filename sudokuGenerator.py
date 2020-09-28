import numpy as np
from random import randint, shuffle

grid = np.zeros((9, 9), np.uint8)  # to see if the problem has any solution
solution = np.zeros((9, 9), np.uint8)  # to restore the solution
difficulty = {'easy': 43, 'intermediate': 49, 'advanced': 53}  # number of blanks
isSolved = False


# see if the number is possible
def possible(y, x, num):
    global grid
    for i in range(9):
        if grid[i][x] == num:
            return False
    for i in range(9):
        if grid[y][i] == num:
            return False
    col = x - x % 3
    row = y - y % 3
    for i in range(3):
        for j in range(3):
            if grid[row + i][col + j] == num:
                return False
    return True


# solve the problem(recursive)- using back tracking algorithm
def solve():
    global isSolved, solution
    if isSolved:
        return
    numbers = np.arange(1, 10)
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                shuffle(list(numbers))
                for num in numbers:
                    if possible(y, x, num):
                        grid[y][x] = num  # solved
                        solve()  # look for another empty element(recursive)
                        grid[y][x] = 0  # if an empty element is not solvable, make the "already solved" states empty
                return  # no number is possible
    isSolved = True
    solution = grid.copy()


def generate(level):  # fill 1-9, shuffle, see if it's right
    global grid, solution, isSolved

    solve()  # create a filled table(=solution)
    game = grid = solution.copy()
    attempts = difficulty[level]

    while attempts > 0:
        row = randint(0, 8)
        col = randint(0, 8)
        if game[row][col] != 0:
            backup = game[row][col]
            game[row][col] = grid[row][col] = 0  # make the cell into 0
            isSolved = False
            solve()  # see if it still has a solution
            if isSolved:
                attempts -= 1
            else:
                game[row][col] = grid[row][col] = backup

    def print_array(x):
        for i in x:
            for j in i:
                if j == 0:
                    j = "_"
                print(j, end='\t')
            print()
        print()

    print("Level:", level)
    print_array(game)
    input("Press any key to check the solution>>")
    print_array(solution)


def start():
    while True:
        num = int(input("Set the difficulty(easy: 0, intermediate: 1, advanced: 2): "))
        if num == 0:
            level = 'easy'
            break
        elif num == 1:
            level = 'intermediate'
            break
        elif num == 2:
            level = 'advanced'
            break
        else:
            print("Please set the difficulty from 0 to 2")
    generate(level)


start()
