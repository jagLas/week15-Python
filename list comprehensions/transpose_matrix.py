# Write your function, here.
def matrix_rows(matrix):
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


print(matrix_rows([[8, 2], [6, 3], [3, 7], [1, 2]]))  #> [[8, 6, 3, 1], [2, 3, 7, 2]]
print(matrix_rows([[1, 4], [3, 2], [1, 0], [9, 7]]))  #> [[1, 3, 1, 9], [4, 2, 0, 7]]
print(matrix_rows([[5, 6], [2, 8], [5, 2], [1, 0]]))  #> [[5, 2, 5, 1], [6, 8, 2, 0]]

# column = {
#   [8, 2],
#   [6, 3],
#   [3, 7],
#   [1, 2]
# }

# row = {
#   [8, 6, 3, 1],
#   [2, 3, 7, 2]
# }