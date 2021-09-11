
# Lists
bikes = ['Yamaha', 'RE', 'Hero']
print(bikes)
print(bikes[2])   # Hero 
# print(bikes[9])   # Error

# Methods
bikes.append('Bajaj') # ['Yamaha', 'RE', 'Hero', 'Bajaj']
print(bikes)

bikes.insert(2, 'TVS')
print(bikes)  # ['Yamaha', 'RE', 'TVS', 'Hero', 'Bajaj']

bikes.extend(['Harley Davidson', 'KTM'])
print(bikes) # ['Yamaha', 'RE', 'TVS', 'Hero', 'Bajaj', 'Harley Davidson', 'KTM']

bikes.pop(1)
print(bikes)  # ['Yamaha', 'TVS', 'Hero', 'Bajaj', 'Harley Davidson', 'KTM']

bikes.remove('KTM')
print(bikes)  # ['Yamaha', 'TVS', 'Hero', 'Bajaj', 'Harley Davidson']

# bikes.clear()
# print(bikes)   # []

print(bikes.index('TVS')) # 1
print(bikes.index('Bajaj')) # 3
# print(bikes.index('KTM')) # ValueError: 'KTM' is not in list

print('KTM' in bikes)  # False
print('Bajaj' in bikes)  # True

print(bikes.count('KTM')) # 0
bikes.append('TVS')
print(bikes.count('TVS')) # 2

bikes.sort()
print(bikes) # ['Bajaj', 'Harley Davidson', 'Hero', 'TVS', 'TVS', 'Yamaha']
bikes.reverse()
print(bikes) # ['Yamaha', 'TVS', 'TVS', 'Hero', 'Harley Davidson', 'Bajaj']

print(sorted(bikes)) # Sorted using Functions => ['Bajaj', 'Harley Davidson', 'Hero', 'TVS', 'TVS', 'Yamaha']

# Slicing
users = ['vengat', 'mano', 'senthil', 'jei', 'meivel', 'karthi']
developers = users  # Both References are same
print(users) # ['vengat', 'mano', 'senthil', 'jei', 'meivel', 'karthi']
print(developers) # ['vengat', 'mano', 'senthil', 'jei', 'meivel', 'karthi']
developers.remove('karthi')
print(users) # ['vengat', 'mano', 'senthil', 'jei', 'meivel']
print(developers) # ['vengat', 'mano', 'senthil', 'jei', 'meivel']

# Slice the list (create new reference)
developers = users[:]
print(users) # ['vengat', 'mano', 'senthil', 'jei', 'meivel']
print(developers) # ['vengat', 'mano', 'senthil', 'jei', 'meivel']
developers.remove('meivel')
print(users) # ['vengat', 'mano', 'senthil', 'jei', 'meivel']
print(developers) # ['vengat', 'mano', 'senthil', 'jei'] (not chaning the original list)

print(list(range(1, 10))) 

# JOIN 
print(" ".join(developers)) # vengat mano senthil jei
print(developers) # ['vengat', 'mano', 'senthil', 'jei']

#List Unpacking
developers.append('meivel')
data_engineer, frontend_developer, *it_developers, backend_developer = developers

print(data_engineer) # vengat
print(frontend_developer) # mano
print(it_developers) # ['senthil', 'jei']
print(backend_developer) # meivel