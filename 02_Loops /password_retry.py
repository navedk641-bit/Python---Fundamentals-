# Password Retry System

correct_password = "python123"

for attempt in range(1, 4):

    password = input("Enter your password: ")

    if password == correct_password:
        print("Login Successful!")
        break

    else:
        remaining = 3 - attempt
        print("Incorrect Password!")

        if remaining > 0:
            print("Attempts remaining:", remaining)
        else:
            print("Account Blocked!")
