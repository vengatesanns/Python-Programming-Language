# Unordered Unique Items
numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9}
numbers2 = {1, 5, 9}
numbers3 = {1, 2, 3, 4, 5}

print(numbers1)

# Methods

# clear()
numbers3.clear()  # Clear the sets
print(numbers3)

# difference()
result = numbers1.difference(numbers2)  # Difference from set1 to set2
print(result)  # {0, 2, 3, 4, 6, 7, 8}
