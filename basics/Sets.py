# Unordered Unique Items
numbers1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 9}
numbers2 = {1, 5, 9}
numbers3 = {1, 2, 3, 4, 5}
numbers1_bkp = numbers1.copy()

print(numbers1)

# Methods

# clear()
numbers3.clear()  # Clear the sets
print(numbers3)

# difference()
result = numbers1.difference(numbers2)  # Difference from set1 to set2
print(result)  # {0, 2, 3, 4, 6, 7, 8}

# discard()
numbers1.discard(5)  # Remove he particular element
print(f"Discarded Set -> {numbers1}")  # Discarded Set -> {0, 1, 2, 3, 4, 6, 7, 8, 9}

# difference_update()
numbers1.difference_update(numbers2)  # update the numbers1 set with difference
print(f"Difference Update -> {numbers1}")  # {0, 2, 3, 4, 6, 7, 8}

# intersection()
print(numbers1_bkp)
print(numbers2)
print(f"Intersection -> {numbers1_bkp.intersection(numbers2)}")  # common items => Intersection -> {1, 5, 9}

# isdisjoint() Should not have common items
print(numbers1_bkp.isdisjoint({11, 10, 11}))  # True
print(numbers1_bkp.isdisjoint(numbers2))  # False

# Union() Combine all the elements b/w the sets
print(numbers1_bkp.union(numbers2))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numbers1_bkp.union({11, 12, 15}))  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15}

# issubset()
print(numbers1_bkp.issubset(numbers2))  # False
print(numbers2.issubset(numbers1_bkp))  # True

# issuperset()
print(numbers1_bkp.issuperset(numbers2))  # True
print(numbers2.issuperset(numbers1_bkp))  # False
