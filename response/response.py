import validators

addr = input("What's your email address? ")
if validators.email(addr):
    print("Valid")
else:
    print("Invalid")