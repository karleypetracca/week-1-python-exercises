# Series of basic dictionary exercises with given dictionary

# Print Elizabeth's phone number.
# Add an entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries.

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

print(phonebook_dict["Elizabeth"])

phonebook_dict["Kareem"] = "938-489-1234"

phonebook_dict.pop("Alice")

phonebook_dict["Bob"] = "968-345-2345"

for i in phonebook_dict:
    print(phonebook_dict[i])

# OR
#print(phonebook_dict.values())