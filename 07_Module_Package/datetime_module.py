import datetime

# Display current date and time
now = datetime.datetime.now()

print("Current Date:", now.date())
print("Current Time:", now.time())

# Calculate age
dob = input("Enter your date of birth (YYYY-MM-DD): ")

birth_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()

today = datetime.date.today()

age = today.year - birth_date.year

if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print("Your Age:", age)
