def check_rows(line):
    for i in range(1,10):
        if line.count(i) != 1:
            return(False)
    return(True)

def make_small_square(grid):       
    square = []
    for i in range(3):
        for j in range(3):
            square.append(grid[i][j])
    return(square)
           
def validSolution(grid):
    for i in grid:
        if check_rows(i) == False:
            return(False) 
    for i in range(9):
        column = []
        for j in grid:
            column.append(j[i])
        if check_rows(column) == False:
            return(False)
    if check_rows(make_small_square(grid)) == False:
        return(False)
    return(True)

