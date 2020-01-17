# Takes a list of numbers and prints the largest number (no user input)

list = [6, 24, 670, 45, 20, 9]

largest = list[0]
for number in list:
    if number > largest:
        largest = number

print("This is the list: ", list)
print("This is the largest: " + str(largest))
