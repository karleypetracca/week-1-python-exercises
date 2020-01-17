# Prints a multiplication table for numbers 1 to 10

start = 1
STOP = 11

while start < STOP:
    for i in range(11):
        answer = start * i
        table_line = "{} x {} = {}".format(start, i, answer)
        print(table_line)
    start += 1