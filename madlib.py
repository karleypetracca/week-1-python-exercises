# Prompts user to input missing words to a madlib-style sentence

# Saves madlib to variable
madlib = "The best show I've ever seen is __(adjective)__ __(noun)__ in which the cast loves to __(verb)__ with a(n) __(noun)__!"

# Shares saved madlib with user
print("Please fill in the blanks for the madlib below:\n", madlib + "\n")

# Saves input from user
adjective = input("What adjective would you like to use?: ").lower()
noun1 = input("What noun would you like to use?: ").lower()
verb = input("What verb would you like to use?: ").lower()
noun2 = input("What noun would you like to use?: ").lower()

# Reformats madlib for use with .format() method
madlib_formatted = madlib.replace("__(adjective)__", "__{}__")
madlib_formatted = madlib_formatted.replace("__(noun)__", "__{}__")
madlib_formatted = madlib_formatted.replace("__(verb)__", "__{}__")

# Shares final madlib result!
print(madlib_formatted.format(adjective, noun1, verb, noun2))