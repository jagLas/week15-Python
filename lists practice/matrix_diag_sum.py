# def diagonalSum(mat):
#     cols = len(mat)
#     rows = len(mat[0])
#     sum = 0

#     for i in range(rows):
#         for j in range(cols):
#             if i == j:
#                 sum += mat[i][j]
#             elif i + j == cols - 1:
#                 sum += mat[i][j]
#     return sum

def diagonalSum(mat):
    rows = len(mat[0])
    total = 0

    for i in range(rows):
        total += mat[i][i]
        total += mat[i][rows - i - 1]
    
    # subtracts out the repeated middle on odd numbered matricies
    if rows % 2 != 0:
        middle = int(rows/2)
        total -= mat[middle][middle]
    return total

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))

mat = [[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print(diagonalSum(mat))