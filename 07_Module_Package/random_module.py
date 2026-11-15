import random
import string

# Generate 6-digit OTP
otp = random.randint(100000, 999999)
print("OTP:", otp)

# Generate random password
characters = string.ascii_letters + string.digits
password = ''.join(random.choice(characters) for i in range(8))
print("Random Password:", password)

# Generate random list numbers
numbers = [random.randint(1, 100) for i in range(5)]
print("Random Numbers:", numbers)
