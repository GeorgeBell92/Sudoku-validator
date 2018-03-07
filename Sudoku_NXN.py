class Sudoku(object):
    
    def __init__(self,object):
        self.A = object
        
    def dimensions(self):
        for i in self.A:
            if len(i)!= len(self.A):
                return(False)
            else:
                pass
        return(True)
    
    def dimensions_int(self):
        r_N = len(self.A)**0.5
        if r_N == int(r_N):
            return(True)
        else:
            return(False)

    def check_rows(self):
        N = len(self.A)
        result = True
        for i in range(1,N+1):
            for j in self.A:
                if j.count(i) != 1:
                    result = False
        return(result)

    def invert_columns(self):
        N = len(self.A)
        result = []
        for i in range(N):
            result.append([])
        for i in range(N):
            for j in self.A:
                result[i].append(j[i])
        return(result)

    def check_columns(self):
        N = len(self.A)
        self.inverted = self.invert_columns()
        result = True
        for i in range(1,N+1):
            for j in self.inverted:
                if j.count(i) != 1:
                    result = False
        return(result)

    def check_small_square(self):
        N = len(self.A)
        square = []
        r_N = int(N**0.5)
        result = True
        for i in range(r_N):
            for j in range(r_N):
                square.append(self.A[i][j])
        for i in range(1,N+1):
            if square.count(i) != 1:
                result = False
        return(result)

    def is_type(self):
        result = True 
        for i in self.A:
            for j in i:
                try:
                    x = int(j)
                    if type(x)!=type(j):
                        result = False
                except ValueError:
                    result = False
        return(result)

        

    def is_valid(self):
        result = True
        if self.dimensions() == False:
            result = False
        elif self.is_type() == False:
            result = False
        elif self.dimensions_int() == False:
            result = False
        elif self.check_small_square() == False:
            result = False
        elif self.check_rows() == False:
            result = False
        elif self.check_columns() == False:
            result = False 
        return(result)
