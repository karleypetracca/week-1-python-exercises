title = "Aye Matey"

STOP = 10

# Display count increase
count = 0
while count < STOP:
    print(count)
    count += 1
print("\n")

# Display by len count of title
count = 0
while count < len(title):
    print(count)
    count += 1
print("\n")

# Display title letters
count = 0
while count < len(title):
    print(title[count])
    count += 1
print("\n")

# Display title letters using modulo
count = 0
while count < len(title):
    if count % 2 == 0:
        print(title[count])
    count += 1
print("\n")

# Display title letters using modulo and remove blank spaces
count = 0
while count < len(title):
    if count % 2 == 0 and title[count] != " ":
        print(title[count])
    count += 1
print("\n")

