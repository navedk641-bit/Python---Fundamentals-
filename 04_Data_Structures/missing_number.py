# Find Missing Number in a List

numbers = [1, 2, 3, 5, 6, 7]

n = 7

expected_sum = n * (n + 1) // 2

actual_sum = sum(numbers)

missing_number = expected_sum - actual_sum

print("Original List:", numbers)
print("Missing Number:", missing_number)
