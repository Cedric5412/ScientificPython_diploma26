import numpy as np
class MyMatrix:
    def __init__(self, n):
        self.n = n
        M = np.random.random((n, n))
        self.M = M

    def inverse(self):
        return np.linalg.inv(self.M)
    
    def determinant(self):
        return np.linalg.det(self.M)
    
    def eigenvalues(self):
        return np.linalg.eig(self.M)
    
    def __add__(self, other):
        result = MyMatrix(self.n)
        result.M = self.M + other.M
        return result
    
    def __mul__(self, other):
        result = MyMatrix(self.n)
        result.M = self.M @ other.M 
        return result

    def __str__(self):
        return f"MyMatrix(n={self.n})\n{self.M}"

N=4
matrix1=MyMatrix(N) #creates a square matrix
matrix2=MyMatrix(N)
print(matrix1.inverse())
print(matrix1.determinant())
print(matrix1.eigenvalues())
print(matrix1+matrix2)
print(matrix1*matrix2)