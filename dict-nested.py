# Series of nested dictionary exercises with given dictionary

# Write a python expression that gets the email address of Ramit.
# Write a python expression that gets the first of Ramit's interests.
# Write a python expression that gets the email address of Jasmine.
# Write a python expression that gets the second of Jan's two interests.


ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

ramit_email_address = ramit["email"]
ramit_interest1 = ramit["interests"][0]
jasmine_email_address = ramit["friends"][0]["email"]
jasmine_interest2 = ramit["friends"][0]["interests"][1]

print(ramit_email_address)
print(ramit_interest1)
print(jasmine_email_address)
print(jasmine_interest2)