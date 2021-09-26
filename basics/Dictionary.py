# Similar to Object (JS) or HashTables (Java)
# Key will Allows only Immutable Objects (List won't allow because it's mutable)
users_data = {
    "name": "Vengat",
    "age": 25,
    "role": ["Data Engineer", "Fullstack Developer"]
}

print(users_data)
print(users_data.get("name"))
print(users_data["name"])
print(type(users_data))  # dict

# Set new Key in to users_data
users_data[(1, 2)] = "Co-ordinates"
print(users_data[(1, 2)])
print(users_data.get((1, 2)))

# methods in dict class

# items() - to grab each item
print(users_data.items())  # return tuple of each item in users_data(dict)

for info in users_data.items():
    print(f"key -> {info[0]}")
    print(f"value -> {info[1]}")

# keys() - to grab only keys

print(users_data.keys())  # return all keys as an array

for key in users_data.keys():
    print(users_data[key])

# clear()
# print(users_data.clear())

# copy()
copied_users_data = users_data.copy()

copied_users_data["name"] = "Senthil"
copied_users_data["role"] = "Software Engineer"

print(copied_users_data)  # Copied and modified dict
print(users_data)  # Original dict

# pop()
print(copied_users_data.pop("name"))  # return value of the key
print(copied_users_data)  # modified dict

# popItem()
print(copied_users_data.popitem())
print(copied_users_data)

# update()
print(copied_users_data.update({"name": "Mano"}))
print(copied_users_data)
