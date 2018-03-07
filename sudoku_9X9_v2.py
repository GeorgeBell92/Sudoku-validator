def check_rows(line):
    for i in range(1,10):
        if line.count(i) != 1:
            return(False)
    return(True)

def invert_columns(grid):
    result = []
    for i in range(9):
        result.append([])   
    for i in range(9):
        for j in grid:
            result[i].append(j[i])
    return(result)

def check_small_square(grid):       
    square = []
    for i in range(3):
        for j in range(3):
            square.append(grid[i][j])
    for i in range(1,10):
        if square.count(i) != 1:
            return(False)
    return(True)
           
def validSolution(grid):
    for i in grid:
        if check_rows(i) == False:
            return(False)
    for i in invert_columns(grid):
        if check_rows(i) == False:
            return(False)                 
    if check_small_square(grid) == False:
        return(False)
    return(True)
