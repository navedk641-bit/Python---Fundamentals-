def power(x, n):
    if n == 0:
        return 1
    else:
        return x * power(x, n - 1)


num = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))

result = power(num, exp)

print("Power =", result)
