# Validates Sudoku in a 9X9 grid

# Create helper functions to seperate the problem into managable portions

# This function checks each row in turn:

def check_rows(grid):
    # Set Default response as true
    result = True
    # Checks that each number between 1 & 9 occurs exactly once
    for i in range(1,10):
        # for each row in the grid
        for j in grid:
            if j.count(i) != 1:
                # If this is not the case, reset result to false
                result = False
    return(result)

# Rather than checking each column, I decided to invert the array.
# I then pass this inverted array into the check_rows function

def invert_columns(grid):
    # set up an empty list
    result = []
    # this creates an empty nested list - [[],[],[],[],[],[],[],[],[]]
    for i in range(9):
        result.append([])
    # i is the column index    
    for i in range(9):
        # for each row (j)
        for j in grid:
            # add the value at the column index, to the corresponding list
            result[i].append(j[i])
    # returns the array
    return(result)

# This could also be done via numpy.transpose

# As stated above, run the inverted array through check_rows

def check_columns(grid):
    return(check_rows(invert_columns(grid)))

# Strictly speaking, this does not need it's own function

# This checks the upper left 'square' within the puzzle

def check_small_square(grid):
    # again, set default as True       
    result = True
    # create an empty list
    square = []
    # This creates a 1X9 array, using the first three numbers
    # of the first three rows
    for i in range(3):
        for j in range(3):
            square.append(grid[i][j])
    # This is essentially the same as in the check_rows function
    for i in range(1,10):
        if square.count(i) != 1:
            result = False
    return(result)

# This runs the other functions to see if the Sudoku is valid
           
def validSolution(item):
    # set default as True. If the puzzle is invalid,
    # the helper functions will set it to False.
    result = True
    if check_rows(item) == False:
        result = False
    if check_small_square(item) == False:
        result = False
    if check_columns(item) == False:
        result = False 
    return(result)
