# Takes a string and prints it in reverse

string_input = input("What string would you like to print in reverse?: ")
string_reverse = ""
for i in range(len(string_input)):
    string_reverse += string_input[-(i+1)]
print(string_reverse)
