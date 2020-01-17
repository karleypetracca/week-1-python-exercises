# Prompts user for number and returns list of factors for that number

user_input = int(input("What number do you want to see factors returned for?: "))
STOP = user_input + 1
count = 1

factor_list = []

while count < STOP:
    for i in range(1, user_input+1):
        if user_input % i == 0:
            factor_list.append(i)
        count += 1
    
print("Here are the factors for {}: {}".format(str(user_input), str(factor_list)))
