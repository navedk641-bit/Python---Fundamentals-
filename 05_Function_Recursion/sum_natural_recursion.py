def sum_natural(n):
    if n == 0:
        return 0
    else:
        return n + sum_natural(n - 1)


num = int(input("Enter a number: "))

result = sum_natural(num)

print("Sum of first", num, "natural numbers is:", result)
