# Takes a string and lengthens double-vowel characters 

vowels = "aeiou"

string_input = input("What string would you like to print with lengthened double-vowels?: ").lower()

string_long_vowels = ""
last_character = ""

for character in string_input:
    if character == last_character and character in vowels:
        string_long_vowels += str(character * 5)
    else:
        string_long_vowels += character
    last_character = character

print(string_long_vowels)
