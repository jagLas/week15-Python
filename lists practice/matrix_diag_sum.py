def diagonalSum(mat):
    cols = len(mat)
    rows = len(mat[0])
    sum = 0

    for i in range(rows):
        for j in range(cols):
            if i == j:
                sum += mat[i][j]
            elif i + j == cols - 1:
                sum += mat[i][j]
    return sum

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))