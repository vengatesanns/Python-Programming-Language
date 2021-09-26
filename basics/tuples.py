# Immutable Lists

user_names_and_ages = ({"Vengat": 26}, {"Mano": 27}, {"Senthil": 27},{"Vengat": 26})
print(user_names_and_ages)
print(user_names_and_ages[0])

# Methods

# Count()
print(user_names_and_ages.count({"Vengat": 26})) # No of times values present

# index()
print(user_names_and_ages.index({"Mano": 27}))
