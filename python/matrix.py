class Matrix():
    def __init__(self, *rows) -> None:
        self.__matrix = []
        if len({len(row) for row in rows}) != 1:
            raise ValueError("Rows cannot have a different number of elements")
        for row in rows:
            self.__matrix.append(row.copy())

    def __repr__(self) -> str:
        result = ""
        for row in self.__matrix:
            result += ", ".join([str(e) for e in row]) + "\n"
        return result[:-1]

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Cannot sum a matrix with {type(other).__name__}")
        if len(self.__matrix) != len(other.__matrix):
            raise ValueError("Cannot sum matrices with different number of rows")
        for row in range(len(self.__matrix)):
            if len(self.__matrix[row]) != len(other.__matrix[row]):
                raise ValueError("Cannot sum matrices with different number of columns")
        return Matrix(*[[self.__matrix[i][j] + other.__matrix[i][j] for j in range(len(self.__matrix[i]))] for i in range(len(self.__matrix))])
    
    def __sub__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f"Cannot subtract a matrix with {type(other).__name__}")
        if len(self.__matrix) != len(other.__matrix):
            raise ValueError("Cannot subtract matrices with different number of rows")
        for row in range(len(self.__matrix)):
            if len(self.__matrix[row]) != len(other.__matrix[row]):
                raise ValueError("Cannot subtract matrices with different number of columns")
        return Matrix(*[[self.__matrix[i][j] - other.__matrix[i][j] for j in range(len(self.__matrix[i]))] for i in range(len(self.__matrix))])
    
    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Matrix(*[[self.__matrix[i][j] * other for j in range(len(self.__matrix[i]))] for i in range(len(self.__matrix))])
        if not isinstance(other, Matrix):
            raise TypeError(f"Cannot multiply a matrix with {type(other).__name__}")
        if len(self.__matrix[0]) != len(other.__matrix):
            raise ValueError("The number of rows in matrix A must be equal to the number of columns in matrix B")
        result = [[0 for b in other.__matrix[0]] for a in self.__matrix]
        for i in range(len(self.__matrix)):
            for j in range(len(other.__matrix[0])):
                for k in range(len(other.__matrix)):
                    result[i][j] += self.__matrix[i][k] * other.__matrix[k][j]
        return Matrix(*result)

    def get_element(self, row, column):
        return self.__matrix[row-1][column-1]

    def remove_row(self, row):
        del self.__matrix[row-1]

    def remove_column(self, column):
        for row in self.__matrix:
            del row[column-1]

    def determinant(self):
        if len(self.__matrix) != len(self.__matrix[0]):
            raise ValueError("Cannot calculate determinant of a non-square matrix")
        if len(self.__matrix) == 2:
            return self.__matrix[0][0] * self.__matrix[1][1] - self.__matrix[1][0] * self.__matrix[0][1]
        result = []
        for a in range(len(self.__matrix)):
            submatrix = Matrix(*self.__matrix)
            submatrix.remove_row(1)
            submatrix.remove_column(a+1)
            result.append(self.__matrix[0][a] * submatrix.determinant())
        return sum([result[i] if i%2==0 else -result[i] for i in range(len(result))])

if __name__ == "__main__":
    matrix = Matrix([1,2,3], [4,5,6], [7,8,9])
    other = Matrix([3,3,3], [1,1,1], [2,2,2])
    print(matrix + other)
    print(matrix - other)
    print(matrix * 2)
    print(matrix * other)
    print(Matrix([1,2], [3,4]).determinant())
    print(matrix.determinant())
    print(Matrix([1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]).determinant())