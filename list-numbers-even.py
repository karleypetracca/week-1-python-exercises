# Takes a list of numbers and prints all even numbers (no user input)

list = [-5, 325, -40, 119, 70, 6]

even_numbers = ""

for number in list:
    if number % 2 == 0:
        even_numbers += str(number) + ", "

even_numbers = even_numbers[:-2]

print("This is the list: ", list)
print("These are the even numbers: " + even_numbers)
