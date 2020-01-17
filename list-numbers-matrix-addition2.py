# Takes two same-sized list matrices and adds their corresponding index 
# numbers together to create a new list matrix (no user input)

matrix1 = [[0, 5], [7, 2], [9, 6]]
matrix2 = [[3, 1], [8, 8], [2, 0]]

new_matrix = []

if len(matrix1) == len(matrix2):
    for i in range(len(matrix1)):
        if len(matrix1[i]) == len(matrix2[i]):
            inner_matrix = []
            for j in range(len(matrix1[i])):
                inner_sum = matrix1[i][j] + matrix2[i][j]
                inner_matrix.append(inner_sum)
            new_matrix.append(inner_matrix)
        else:
            print("Inner matrices must be the same size!")
    print("These are the list matrices:\n", matrix1, "\n", matrix2)
    print("This is the new list matrix: ", new_matrix)
else:
    print("Matrices must be the same size!")