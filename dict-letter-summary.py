# Prompts user for word and prints dictionary containing tally of how many
# times each letter in alphabet was used in the word

user_input = input("What word would you like to submit?: ")

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
letter_summary = {}

for i in alphabet:
    if i in user_input:
        letter_sum = user_input.count(i)
        letter_summary[i] = letter_sum

print(letter_summary)
