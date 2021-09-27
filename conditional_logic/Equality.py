# == vs is
# == for value equality check but "is" keyword is used for check whether same memory location

print(True == 1)  # True
print('1' == 1)  # False
print([] == [])  # True

# is (check for memory reference

print(True is 1)  # False
print("1" is 1)  # False
print([] is [])  # False
print(True is True)  # True

# Realtime example
print("Realtime Examples")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print(list1 == list2)  # True
print(list1 is list2)  # False

list3 = list1

print(list1 == list3)  # True
print(list1 is list3)  # True

list4 = list1[:]

print(list1 == list4)  # True
print(list1 is list4)  # False
