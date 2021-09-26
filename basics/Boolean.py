# True or False

isValid = True
print(type(isValid))  # Bool

isValid = False
print(isValid)  # False

# Conversion
print(bool(1))  # True
print(bool(0))  # False

# Truthy
print(bool('Vengat'))  # True
print(bool(3))  # True
print(bool('True'))  # True
print(bool('False'))  # True

# Falsey
print(bool(None))  # False
print(bool(''))  # False
print(bool({}))  # False
print(bool([]))  # False
