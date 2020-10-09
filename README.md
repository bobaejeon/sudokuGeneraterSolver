# Sudoku Generater
Hello world! This is a simple sudoku generater and solver in python.

### How to generate a game?
  1. Get a fully solved board
 > *It will be on a loop of erasing numbers according to the difficulty user have set*
  2. Erase one cell at a time(by randomly chosen row and column)
  3. See if it still has a solution<br>
    3-1. If so, goto step 2 and repeat<br>
    3-2. If not, make the cell filled again and goto step 2 and repeat
  4. Print out the game board, it's time to play!
  
### How to solve it?
  I used backtracking algorithm with recursive function. <br>
  If there's a "blank", it will test with numbers from 1 to 9 to see which number fits the sudoku rule. <br>

<details markdown="1">
<summary>Do you want to see how I suffered?</summary>

  My first approach to generate a sudoku puzzle was to put random numbers in randomly chosen rows and columns.<br>
  So basically I tried put some numbers instead of a full grid.<br>
  <br>
  Even if the numbers you fill in fit the rules, it may be a game with no correct answer at all.<br>
  (Well it seems more normal to have no correct answer)<br>
 <br>
  Also this approach took so much time on creating random numbers.<br>
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
