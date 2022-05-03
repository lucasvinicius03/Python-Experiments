class Matrix():
    def __init__(self, size, *values:int) -> None:
        if len(values) != size[0] * size[1]:
            raise ValueError("Vector has more or less elements than inputed size")
        values = iter(values)
        self.__matrix = [[next(values) for a in range(size[1])] for b in range(size[0])]
        self.size_l = size[0]
        self.size_c = size[1]

    def __repr__(self) -> str:
        return str(self.__matrix)

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Cannot sum a matrix with {type(other).__name__}")
        try: return Matrix((self.size_l, self.size_c), *self.undo_matrix([[self.__matrix[a][b] + other.__matrix[a][b] for b in range(self.size_c)] for a in range(other.size_l)]))
        except IndexError: raise ValueError("Cannot sum matrices with different number of rows or columns")
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Cannot subtract a matrix with {type(other).__name__}")
        try: return Matrix((self.size_l, self.size_c), *self.undo_matrix([[self.__matrix[a][b] - other.__matrix[a][b] for b in range(self.size_c)] for a in range(other.size_l)]))
        except IndexError: raise ValueError("Cannot subtract matrices with different number of rows or columns")
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix(*[[self.__matrix[i][j] * other for j in range(len(self.__matrix[i]))] for i in range(self.size_l)])
        if not isinstance(other, Matrix):
            raise TypeError(f"Cannot multiply a matrix with {type(other).__name__}")
        try: return Matrix((self.size_l, other.size_c), *self.undo_matrix([[sum([self.__matrix[c][a] * other.__matrix[a][b] for a in range(self.size_c)]) for b in range(other.size_c)] for c in range(self.size_l)]))
        except IndexError: raise ValueError("The number of rows in matrix A must be equal to the number of columns in matrix B")

    def get_element(self, row, column):
        return self.__matrix[row-1][column-1]

    def remove_row(self, row):
        del self.__matrix[row-1]
        self.size_l -= 1

    def remove_column(self, column):
        for row in self.__matrix:
            del row[column-1]
        self.size_c -= 1

    def replace_row(self, row, new_row):
        if len(self.__matrix[row-2]) != len(new_row):
            raise ValueError("Current row and new row have different lengths")
        self.__matrix[row-1] = new_row.copy()

    def replace_column(self, column, new_column):
        if self.size_l != len(new_column):
            raise ValueError("Current column and new column have different lengths")
        for row in range(self.size_l):
            self.__matrix[row][column-1] = new_column[row]

    def determinant(self):
        if self.size_l != self.size_c:
            raise ValueError("Cannot calculate determinant of a non-square matrix")
        if self.size_l == 1:
            return self.__matrix[0][0]
        result = []
        for a in range(self.size_l):
            submatrix = Matrix((self.size_l, self.size_c), *self.undo_matrix())
            submatrix.remove_row(1)
            submatrix.remove_column(a+1)
            result.append(self.__matrix[0][a] * submatrix.determinant())
        return sum([result[i] if i%2==0 else -result[i] for i in range(len(result))])

    def cramer(self, result):
        if isinstance(result, Matrix):
            result = [x[0] for x in result.__matrix]
        if self.size_l != self.size_c:
            raise ValueError("Matrix must be square")
        if self.size_l != len(result):
            raise ValueError("Result matrix must have n values for a nxn variable matrix")
        d = self.determinant()
        if d == 0: return None
        determinants = []
        for value in range(len(result)):
            submatrix = Matrix((self.size_l, self.size_c), *self.undo_matrix())
            submatrix.replace_column(value+1, result)
            determinants.append(submatrix.determinant())
        if d != 0:
            return [a / d for a in determinants]
        if not all(determinants):
            return -1
        return 0
        
    def undo_matrix(self, other = None):
        if other == None:
            return [self.__matrix[a][b] for a in range(self.size_l) for b in range(self.size_c)]
        return [other[a][b] for a in range(len(other)) for b in range(len(other[0]))]

if __name__ == "__main__":
    def multiplicar(matriz_a, matriz_b):
        try: return [[sum([matriz_a[c][a] * matriz_b[a][b] for a in range(len(matriz_a[0]))]) for b in range(len(matriz_b[0]))] for c in range(len(matriz_a))]
        except IndexError: print("Não é possível multiplicar essas matrizes")
        
    def soma(matriz_a, matriz_b):
        try: return [[matriz_a[a][b] + matriz_b[a][b] for b in range(len(matriz_a[0]))] for a in range(len(matriz_a))]
        except IndexError: print("Não é possível somar essas matrizes")

    def subtracao(matriz_a, matriz_b):
        try: return [[matriz_a[a][b] - matriz_b[a][b] for b in range(len(matriz_a[0]))] for a in range(len(matriz_a))]
        except IndexError: print("Não é possível subtrair essas matrizes")

    def visualizar(matriz):
        [print(*linha) for linha in matriz]

    matrizA = Matrix((3, 3), 1,2,3,4,5,6,7,8,9)
    matrizB = Matrix((3, 3), 2,3,4,5,6,7,8,9,10)
    matrizC = Matrix((2,3), 1,2,3,4,5,6)
    matrizD = Matrix((2,3), 7,8,9,10,11,12)
    matrizE = Matrix((3,3), 67, 5, 3, 4, 7, 0, 7 ,55, 433)
    print(matrizA)
    print(matrizB)
    print(matrizC)
    print(matrizD)
    print(matrizA + matrizB)
    print(matrizC + matrizD)
    print(matrizA - matrizB)
    print(matrizC - matrizD)
    print(matrizA * matrizB)
    print(matrizC * matrizA)
    print(matrizA.determinant())
    print(matrizB.determinant())
    print(matrizE.determinant())
    x, y, z = matrizE.cramer((124, 421, 1231))
    print(x, y, z)