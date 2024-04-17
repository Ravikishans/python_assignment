password=input("Enter your password: ")

import string

def check_password_strength(password):
    if len(password)<8:
        return "Weak password! \n Password should be at least 8 characters long"
    uppercase=any(char.isupper() for char in password)
    lowercase=any(char.islower() for char in password)
    digits=any(char.isdigit() for char in password)
    special=any(char in string.punctuation for char in password)
    space=any(char in string.whitespace for char in password)

    if uppercase and lowercase and digits and (special or space):
        return "strong password"
    else:
        return "Weak password! \n Password should include at least one uppercase letter, one lowercase letter, one digit, and one special character"

print("The password is a", check_password_strength(password))


