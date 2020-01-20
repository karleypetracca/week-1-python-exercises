# Takes items ordered, calculates suggested tip and tax, and prints receipt 
# with totals (no user input)

# Menus
menu = {
 "Brunch" : {
    "Steak and Eggs": 16.99,
    "Three Egg Breakfast": {
        "Without Bacon": 8.99,
        "With Bacon": 9.99
    },
    "Egg Benedict": 11.99,
    "Biscuit and Gravy": 7.99,
    "Chicken Fingers": 10.99,
    "Chicken Wrap": 8.99,
    "Steak Salad" : 15.99
 },
 "Drinks": {
    "Soft Drink": 1.99,
    "Coffee": 1.99,
    "Orange Juice": 0.99,
    "Milk": 0.55,
    "Water": 0.00
 },
 "Specials": {
    "Soup of the Day": 8.99,
    "Catch of the Day": 14.99,
    "Chef Special": 15.99
 }
}


# Table 1 order
T1_guest1 = ["Egg Benedict", "Coffee"]
T1_guest2 = ["Biscuit and Gravy", "Coffee"]
T1_guest3 = ["Steak and Eggs", "Soft Drink"]
T1 = {"Guest 1": T1_guest1, "Guest 2": T1_guest2, "Guest 3": T1_guest3}


# Table 2 order
T2_guest1 = ["Steak Salad", "Soft Drink"]
T2_guest2 = ["Soup of the Day", "Chicken Wrap", "Water"]
T2_guest3 = ["Chicken Fingers", "Soft Drink"]
T2_all = ["Chef Special"]
T2 = {"Guest 1": T2_guest1, "Guest 2": T2_guest2, "Guest 3": T2_guest3, "Table": T2_all}


# Function receipt print-out
def print_receipt(table_order):
    print("*" * 25)
    subtotal = 0
    for guest, order in table_order.items():
        print ("*** {} ***".format(guest))
        for value in order:
            if menu["Brunch"].get(value, 0) != 0:
                subtotal += menu["Brunch"][value]
                print("{:<25} $ {:>6,.2f}".format(value + ":", menu["Brunch"].get(value)))
            if menu["Drinks"].get(value, 0) != 0:
                subtotal += menu["Drinks"][value]
                print("{:<25} $ {:>6,.2f}".format(value + ":", menu["Drinks"].get(value)))
            if value == "Water":
                print("{:<25} $ {:>6}".format(value + ":", "0.00"))
            if menu["Specials"].get(value, 0) != 0:
                subtotal += menu["Specials"][value]
                print("{:<25} $ {:>6,.2f}".format(value + ":", menu["Specials"].get(value)))
        print()
    
    tax = subtotal * 0.07
    total = subtotal + tax

    print()
    print("{:<19}Price: $ {:>6,.2f}".format("", subtotal))
    print("{:<19}Taxes: $ {:>6,.2f}".format("", tax))
    print("{:<19}Total: $ {:>6,.2f}".format("", total))

    print()
    print()
    print("**Suggested Tip**")
    print(" Tip 25%:  ${:>6,.2f}".format(total * 0.25))
    print(" Tip 20%:  ${:>6,.2f}".format(total * 0.20))
    print(" Tip 15%:  ${:>6,.2f}".format(total * 0.15))
    

# Final print for testing
print_receipt(T1)
print("\n"*3)
print_receipt(T2)