# Takes a list of numbers and a number to multiply by, and creates a new list 
# of the multiplied numbers (no user input)

list = [-5, 325, -40, 119, 70, 6]
multiply_by = 3

multiplied_list = []
for number in list:
    multiplied_list.append(number * multiply_by)

print("This is the list: ", list)
print("This is the number to multiply by: ", multiply_by)
print("These are the multiplied numbers: ", multiplied_list)
