class Sudoku(object):
    
    def __init__(self,object):
        
        self.A = object
        self.N = len(self.A)
        self.r_N = int(self.N ** 0.5)

    def check_1toN(self,item):
        for i in range(1,self.N + 1):
            if item.count(i) != 1:
                return(False)
        return(True)
    
    def check_dimensions(self):
        for i in self.A:
            if len(i)!= self.N:
                return(False)
        if self.r_N != self.N**0.5:
            return(False)
        return(True)

    def make_small_square(self):
        square = []
        for i in range(self.r_N):
            for j in range(self.r_N):
                square.append(self.A[i][j])
        return(square)

    def is_type(self): 
        for i in self.A:
            for j in i:
                try:
                    x = int(j)
                    if type(x)!=type(j):
                        return(False)
                except ValueError:
                    return(False)
        return(True)

    def is_valid(self):
        if self.check_dimensions() == False:
            return(False)
        elif self.is_type() == False:
            return(False)
        else:
            for i in self.A:
                if self.check_1toN(i) == False:
                    return(False)               
            for i in range(self.N):
                column = []
                for j in self.A:
                    column.append(j[i])
                if self.check_1toN(column) == False:
                    return(False)
            if self.check_1toN(self.make_small_square()) == False:
                return(False)
        return(True)
