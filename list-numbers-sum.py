# Takes a list of numbers and prints their sum (no user input)

list = [6, 24, 670, 45, 20, 9]

number_sum = 0
for number in list:
    number_sum += number

print("This is the list: ", list)
print("This is the sum: " + str(number_sum))
