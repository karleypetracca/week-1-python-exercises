power_rangers = ["Jason", "Trini", "Zack", "Billy", "Kim", "Tommy"]
print("Here are the power rangers!: " + str(power_rangers))
user_input = input("Who would you like to remove?: ")

# Checks if user_input is in power_rangers and removes if yes
if user_input in power_rangers:
    power_rangers.remove(user_input)
    print(power_rangers)
else:
    print("{} isn't part of the group".format(user_input))