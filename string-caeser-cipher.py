# Takes a caeser sipher string with offset of 13 and deciphers the string

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

caeser_sipher = input("What string would you like to print in leetspeak?: ").lower()
decipher = ""
for character in caeser_sipher:
    if character in alphabet:
        decipher += alphabet[alphabet.index(character)+13]
    else:
        decipher += character

final_decipher = decipher.capitalize()
print(final_decipher)
