power_rangers = ["Jason", "Trini", "Zack", "Billy", "Kim", "Tommy"]
print("Here are the power rangers!: " + str(power_rangers))
check = "Tommy"

# Checks if character is in power_rangers
if check in power_rangers:
    print("Success!")
else:
    print("Fail")

# Checks if character is in power_rangers and removes if yes
if check in power_rangers:
    power_rangers.remove(check)
    print(power_rangers)
else:
    print("Tommy isn't part of the group")