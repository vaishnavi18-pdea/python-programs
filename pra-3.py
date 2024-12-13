def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
def add_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] + B[i][j]
    return C
def subtract_matrices(A, B):
    rows = len(A)
    cols = len(A[0])
    C = [[0 for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            C[i][j] = A[i][j] - B[i][j]
    return C
def multiply_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must be equal to number of rows in B.")
    rows_A = len(A)
    cols_B = len(B[0])
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            C[i][j] = sum(A[i][k] * B[k][j] for k in range(len(A[0])))
    return C
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
A = [
    [1, 2, 3],
    [4, 5, 6],
    [24, 20, 30]
]
B = [
    [7, 8, 9],
    [10, 11, 12],
    [1, 2, 3]
]
print("Matrix A:")
print_matrix(A)
print("A + B:")
C = add_matrices(A, B)
print_matrix(C)
print("A - B:")
D = subtract_matrices(A, B)
print_matrix(D)
print("A * B:")
E = multiply_matrices(A, B)
print_matrix(E)
print("Transpose of A:")
F = transpose_matrix(A)
print_matrix(F)
