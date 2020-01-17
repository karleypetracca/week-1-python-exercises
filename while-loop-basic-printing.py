# Prints numbers 1 to 10 (inclusive)

count_range = 1
while count_range < 11:
    print(count_range)
    count_range += 1



# Prints numbers based on range provided from user

start = int(input("What number should we start on?: "))
STOP = int(input("What number should we stop on (inclusive)?: "))+1

while start < STOP:
    print(start)
    start += 1



# Prints each odd number between 1 and 10 (inclusive)

count_range = 1
while count_range < 11:
    if count_range % 2 == 0:
        count_range += 1
    else:
        print(count_range)
        count_range += 1