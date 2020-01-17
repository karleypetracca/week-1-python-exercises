# Takes a string and prints it in leetspeak

original_conversion = "AEGIOST"
leetspeak_conversion = "4361057"

string_input = input("What string would you like to print in leetspeak?: ").upper()
string_leetspeak = ""
for character in string_input:
    add_status = False
    for i in range(len(original_conversion)-1):
        if character == original_conversion[i] and add_status == False:
            string_leetspeak += leetspeak_conversion[i]
            add_status = True
        elif character not in original_conversion and add_status == False:
            string_leetspeak += character
            add_status = True

print(string_leetspeak)
