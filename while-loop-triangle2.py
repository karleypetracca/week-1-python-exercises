# Prints a triangle N lines tall as specified by the user

height = int(input("What height should the triangle be?: "))
middle = 1

while height > 0:
    print(" " * (height-1) + "*" * middle + " " * (height-1))
    height -= 1
    middle += 2
