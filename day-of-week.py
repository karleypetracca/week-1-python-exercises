# Returns name of the day of week based on number of day in week
# Example: Sunday is 1
# Example: Friday is 6

day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day_num = int(input("What day number would you like to submit: \n*** please choose a number between 1 to 7 ***\n")) - 1

print (day_list[day_num])
