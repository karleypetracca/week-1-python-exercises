# Takes two 2x2 list matrices and multiplies them based on the official 
# mathematic method to create a new list matrix  (no user input)

matrix1 = [[7, 2], [9, 6]]
matrix2 = [[3, 1], [8, 8]]

value1 = matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]
value2 = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]
value3 = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
value4 = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]

new_matrix = [[value1, value2], [value3, value4]]

print("These are the list matrices:\n", matrix1, "\n", matrix2)
print("This is the new list matrix: ", new_matrix)
