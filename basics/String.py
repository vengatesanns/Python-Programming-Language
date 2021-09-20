# Basic Declaration and Initialization

user_name = "vengat"
user_id = '123'

print(user_name)
print(user_id)

# Escape Sequence
greetings = "Welcome to \"HackPro-Tech\" youtube Channel!"
print(greetings)

# Formatted String (Kind of String Interpolation or Similar to JavaScript back-tick ``)
youtube_user_name = 'Vengat'
youtube_channel = 'HackPro-Tech'

print(f'{youtube_user_name} owned the {youtube_channel} youtube channel!')

# Index in the String
print(youtube_user_name[4])  # a
print(youtube_user_name[1:5])  # enga
print(youtube_user_name[1:5:2])  # eg
print(youtube_user_name[1:])  # engat
print(youtube_user_name[:4])  # Veng
print(youtube_user_name[::2])  # Vna
print(youtube_user_name[-1])  # t
print(youtube_user_name[:-5:-1])  # tagn
print(youtube_user_name[::-1])  # tagneV
