# Prompts user for sentence and prints dictionary containing tally of how many
# times each word was used in the sentence

user_input = input("What sentence would you like to submit?: ").lower()

word_split = user_input.split(" ")

word_summary = {}

for i in word_split:
    if i in user_input:
        word_sum = user_input.count(i)
        word_summary[i] = word_sum

print(word_split, word_summary)
