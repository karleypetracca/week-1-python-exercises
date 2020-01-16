# Prompts user to input total bill and level of service to calculate tip, with
# added ability to divide the check

bill_amount = float(input("What was the bill amount (before tax)?:  $"))

service_level = input("What was the level of service? (Options: bad, fair, good):  ").lower()

divide_check = ""

while divide_check != "Y" and divide_check != "N":
    divide_check = input("Would you like to divide the check? (Y/N):  ")

if service_level == "bad":
    tip_amount = 0.10 * bill_amount
if service_level == "fair":
    tip_amount = 0.15 * bill_amount
if service_level == "good":
    tip_amount = 0.20 * bill_amount

total_bill = bill_amount + tip_amount

if divide_check == "Y":
    division_number = int(input("How many people should we divide this check for?:  "))
    tip_amount_per_person = tip_amount / division_number
    total_bill_per_person = total_bill / division_number
    print("\nTip amount: $%.2f" % (tip_amount))
    print("Total bill: $%.2f" % (total_bill))
    print("Tip amount per person: $%.2f" % (tip_amount_per_person))
    print("Total bill per person: $%.2f" % (total_bill_per_person))
elif divide_check == "N":
    print("\nTip amount: $%.2f" % (tip_amount))
    print("Total bill: $%.2f" % (total_bill))
    