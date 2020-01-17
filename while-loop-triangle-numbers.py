# Prompts user for triangle height and returns triangle number

user_input = int(input("What triangle height (or width) do you want to get the triangle number for?: "))

triangle_number = 0
STOP = user_input + 1

while triangle_number < STOP:
    for i in range(STOP):
        triangle_number += i

print("The triangle number is: " + str(triangle_number))
