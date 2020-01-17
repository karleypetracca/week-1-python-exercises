# Takes a list of numbers and creates a new list that contains all numbers 
# greater than zero (no user input)

list = [-5, 325, -40, 119, 70, 6]

positive_numbers = []
for number in list:
    if number > 0:
        positive_numbers.append(number)

print("This is the list: ", list)
print("These are the positive numbers: ", positive_numbers)
