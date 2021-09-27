my_list = ['Vengat', "Mano", "Senthil", "Jei", "Vengat", "Jei", "Mano"]

duplicates = set()

for user in my_list:
    if my_list.count(user) > 1:
        duplicates.add(user)

print(duplicates)
