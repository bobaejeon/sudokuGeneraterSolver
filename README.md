# Sudoku Generater
Hello world! This is a simple sudoku generater and solver in python.

### How to generate a game?
  1. Get a fully solved board
 >> <br>*It will be on a loop of erasing numbers according to the difficulty user have set*<br>
  2. Erase one cell at a time(by randomly chosen row and column)
  3. See if it still has a solution
    3-1. If so, goto step 2 and repeat
    3-2. If not, make the cell filled again and goto step 2 and repeat
  4. Print out the game board, it's time to play!
  
### How to solve it?
  I used backtracking algorithm with recursive function. 
  If there's a "blank", it will test with numbers from 1 to 9 to see which number fits the sudoku rule. 

<details markdown="1">
<summary>Do you want to see how I suffered?</summary>

  My first approach to generate a sudoku puzzle was to put random numbers in randomly chosen rows and columns.
  So basically I tried put some numbers instead of a full grid.
  
  Even if the numbers you fill in fit the rules, it may be a game with no correct answer at all.
  (Well it seems more normal to have no correct answer)
 
  Also this approach took so much time on creating random numbers.
```````
# (wrong)generate a problem
def generate():  
    global grid
    level = np.random.randint(27, 31)
    while level > 0:
        x = np.random.randint(0, 9)
        y = np.random.randint(0, 9)
        if grid[y][x] != 0:
            continue
        num = np.random.randint(1, 10)
        if possible(y, x, num):
            grid[y][x] = num
            level -= 1
        
      ...and so on
``````
</details>
  
### Screenshot
