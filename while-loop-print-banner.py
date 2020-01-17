# Prints a banner based on user input

banner_text = "* " + input("What text do you want to put on the banner?: ") + " *"

banner_border = ""

while len(banner_border) < len(banner_text):
    banner_border += "*"

print(banner_border)
print(banner_text)
print(banner_border)
