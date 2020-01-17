# prints a NxN box specified by the user (borders only)

height = int(input("What should the box height be?: "))
width = int(input("What should the box width be?: "))

top_and_bottom = "*" * width + "\n"
middle = "*" + (" " * (width-2)) + "*" + "\n"

print(top_and_bottom)
while height > 2:
    print(middle)
    height -= 1
print(top_and_bottom)
