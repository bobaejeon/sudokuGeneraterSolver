# Sudoku Generater
Hello world! This is a simple sudoku generater and solver in python.

### How to generate?
  1. Get a fully solved board
  *It will be erasing numbers according to the difficulty user have set*
  2. Erase one cell at a time(by randomly chosen row and column)
  3. See if it still has a solution
    3-1. If so, goto step 2 and repeat
    3-2. If not, make the cell filled again and goto step 2 and repeat
  4. Print out the game board, it's time to play!
  
### How to solve?
  I used backtracking algorithm with recursive function. 
  If there's a "blank", it will test with numbers from 1 to 9 to see which number fits the sudoku rule. 

#### Do you want to see how I suffered?
  My first approach to generate a sudoku puzzle was to put random numbers in randomly chosen rows and columns.
  예를 들어 한 30칸만 채운다면, 채운 데는 다 규칙에 맞았어도 결국 답이 없을 수 있다.
 
  This approach took so much time on creating random numbers.
  And even I checked the number was possible by then, 
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
        
      ay = np.array(5)
      for y in range(5):
            while True:
                  num = np.random.randint(0, 10)
                  ay[y] = num
                  for i in range(1, y+1): 
                        

            for x in range(9):
                  while True:
                      num = np.random.randint(0, 10)
                      if possible(y, x, num):
                            print(y,", ",x,", ",num, ", ",possible(y, x, num))
                            grid[y][x] = num
                            break
      print(grid)
     
``````
### Screenshot
