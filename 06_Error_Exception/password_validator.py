class PasswordError(Exception):
    pass


try:
    password = input("Enter your password: ")

    if len(password) < 8:
        raise PasswordError("Password must be at least 8 characters long.")

    if not any(ch.isupper() for ch in password):
        raise PasswordError("Password must contain an uppercase letter.")

    if not any(ch.isdigit() for ch in password):
        raise PasswordError("Password must contain a number.")

    print("Password is valid!")

except PasswordError as e:
    print("Error:", e)
