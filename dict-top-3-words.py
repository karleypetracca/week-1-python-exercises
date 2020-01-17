# Prompts user for sentence and prints dictionary containing top three words used

user_input = input("What sentence would you like to submit?: ").lower()
user_input = "To be or not to be do be do be do".lower()

word_split = user_input.split(" ")

word_summary = {}

for i in word_split:
    if i in user_input:
        word_sum = user_input.count(i)
        word_summary[i] = word_sum

print(word_summary)

top1, top2, top3 = ["",0], ["",0], ["",0]

for key, value in word_summary.items():
    if value >= top1[1]:
        top3 = [top2[0], top2[1]]
        top2 = [top1[0], top1[1]]
        top1 = [key, value]
    elif value >= top2[1]:
        top3 = [top2[0], top2[1]]
        top2 = [key, value]
    elif value >= top3[1]:
        top3 = [key, value]

print("%s: %s" % (top1[0], top1[1]))
print("%s: %s" % (top2[0], top2[1]))
print("%s: %s" % (top3[0], top3[1]))
