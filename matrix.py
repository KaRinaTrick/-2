def get_matrix (n, m, value):
    matrix = []
    for j in range (0,n):
        matrix_line = []
        for i in range (0,m):
            matrix_line.append(value)
        matrix.append(matrix_line)
        if value <= 0:
            matrix = []
    return matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
result4 = get_matrix(4, 2, 15)
result5 = get_matrix(4, 2, 0)
print(result1)
print(result2)
print(result3)
print(result4)
print(result5)

