# Takes two 2x2 list matrices and adds their corresponding index numbers
# together to create a new list matrix (no user input)

matrix1 = [[0, 5], [7, 2]]
matrix2 = [[3, 1], [8, 8]]

new_matrix1 = matrix1[0][0] + matrix2[0][0]
new_matrix2 = matrix1[0][1] + matrix2[0][1]
new_matrix3 = matrix1[1][0] + matrix2[1][0]
new_matrix4 = matrix1[1][1] + matrix2[1][1]
new_matrix = [[new_matrix1, new_matrix2], [new_matrix3, new_matrix4]]

print("These are the list matrices:\n", matrix1, "\n", matrix2)
print("This is the new list matrix: ", new_matrix)
