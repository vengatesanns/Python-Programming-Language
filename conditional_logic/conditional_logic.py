# if - elif - else

account_found = True
is_authenticated = False

if account_found & is_authenticated:
    print("Logged in successfully!")
elif account_found or is_authenticated:
    print("Authentication Denied, Make sure everything is correct")
else:
    print("Please go head and create an account")
