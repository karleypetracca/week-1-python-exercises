# prints a triangle 4 lines tall

height = 4
middle = 1

while height > 0:
    print(" " * (height-1) + "*" * middle + " " * (height-1))
    height -= 1
    middle += 2
