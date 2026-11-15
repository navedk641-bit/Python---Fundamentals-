# LCM and HCF Using Loops

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find HCF
a = num1
b = num2

while b != 0:
    remainder = a % b
    a = b
    b = remainder

hcf = a

# Find LCM
if num1 == 0 or num2 == 0:
    lcm = 0
else:
    lcm = abs(num1 * num2) // abs(hcf)

print("HCF =", abs(hcf))
print("LCM =", lcm)
