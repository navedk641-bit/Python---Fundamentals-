# Count Frequency of Elements Using Dictionary

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Original List:", numbers)
print("Frequency of Elements:")

for key, value in frequency.items():
    print(key, ":", value)
