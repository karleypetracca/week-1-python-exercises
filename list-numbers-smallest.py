# Takes a list of numbers and prints the smallest number (no user input)

list = [6, 24, 670, 45, 20, 9]

smallest = list[0]
for number in list:
    if number < smallest:
        smallest = number

print("This is the list: ", list)
print("This is the smallest: " + str(smallest))
