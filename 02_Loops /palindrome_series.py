# Print Palindrome Numbers in a Given Range

start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

print("Palindrome numbers are:")

for num in range(start, end + 1):

    if str(num) == str(num)[::-1]:
        print(num, end=" ")
        
print()
