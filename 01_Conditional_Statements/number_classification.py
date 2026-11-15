# Number Classification

num = int(input("Enter a number: "))

# Positive, Negative or Zero
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# Even or Odd
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# Divisibility by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is not divisible by both 3 and 5")
