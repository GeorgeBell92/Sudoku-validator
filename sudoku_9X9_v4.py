def check_rows(line):
    for i in range(1,10):
        if line.count(i) != 1:
            return(False)
    return(True)

def check_small_square(grid):       
    for i in range(1,10):
        if grid[0:3,0:3].count(i) != 1:
            return(False)
    return(True)
           
def validSolution(grid):
    for i in grid:
        if check_rows(i) == False:
            return(False)
    for i in range(9):
        if check_rows(grid[i]) == False:
            return(False)                 
    if check_small_square(grid) == False:
        return(False)
    return(True)
