# Returns whether user should work or sleep in based on whether number of day 
# in week corresponds to weekday or weekend, respectively
# Example: Sunday is 1, which is a weekend
# Example: Friday is 6, which is a weekday

day_num = int(input("What day number would you like to submit: \n*** please choose a number between 1 and 7 ***\n"))

if day_num > 1 and day_num < 7:
    work_or_sleep = "Go to work"
else:
    work_or_sleep = "Sleep in"

print (work_or_sleep)
