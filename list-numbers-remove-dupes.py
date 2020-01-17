# Takes a list and creates a new list with duplicates removed (no user input)

input_list = ["apple", "hello", "hello", 2, "apple"]

dupes_removed = []

for value in input_list:
    if value not in dupes_removed:
        dupes_removed.append(value)

print("This is the list:\n", input_list)
print("This is the list without duplicates:\n", dupes_removed)
