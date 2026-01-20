from validator_collection import validators
e = input("What's your email address? ")
try:
    if validators.email(e):
        print("Valid")
except:
    print("Invalid")
