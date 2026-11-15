Check Prime Number Using Function

def is_prime(n):
if n <= 1:
return False

for i in range(2, n):
    if n % i == 0:
        return False

return True

number = 17

if is_prime(number):
print(number, "is a Prime Number")
else:
print(number, "is not a Prime Number")
