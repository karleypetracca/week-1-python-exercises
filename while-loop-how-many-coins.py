# Prompts user for whether they want a coin (Y/N), giving one coin for each yes
# and printing final tally when user prompts no.

coin_tally = 0
want_coin = True

while want_coin == True:
    user_input = input("Would you like a coin? (Y/N): ")
    if user_input == "Y":
        coin_tally += 1
        print("You have: {}".format(str(coin_tally)))
    elif user_input == "N":
        print("Final tally: {}".format(str(coin_tally)))
        print("Goodbye!")
    else:
        print("Please respond with Y or N!")        
