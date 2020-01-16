# Prompts user to input name and replies hello in all caps

name = input("What is your name?: ").upper()

print("HELLO, {}!".format(name))
print("YOUR NAME HAS {} LETTERS IN IT! AWESOME!".format(len(name)))