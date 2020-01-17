# Takes two vectors and multiplies each vector by its corresponding number, 
# creating a new list (no user input)

vector1 = [-5, 32, 40]
vector2 = [6, 52, -3]

multiplied_list = []
for i in range(len(vector1)):
    multiplied_list.append(vector1[i] * vector2[i])

print("These are the vector lists: ", vector1, " ", vector2)
print("These are the multiplied numbers: ", multiplied_list)
