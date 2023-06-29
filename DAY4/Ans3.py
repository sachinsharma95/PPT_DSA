def transpose_matrix(matrix):
    n = len(matrix)  # number of rows
    m = len(matrix[0])  # number of columns

    # Initialize result matrix
    result = [[0] * n for _ in range(m)]
   
    # Transpose the matrix
    for i in range(n):
        for j in range(m):
            result[j][i] = matrix[i][j]

    return result


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = transpose_matrix(matrix)
print(result)
