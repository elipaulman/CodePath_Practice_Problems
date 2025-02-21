def transpose(matrix):
    result = [[0] * len(matrix) for _ in range(len(matrix[0]))]
    result = [[0] * len(matrix) for _ in r]
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            result[c][r] = matrix[r][c]
    print(result)
       
       
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix1)

matrix2 = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix2)     
        