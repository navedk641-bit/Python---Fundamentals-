# List Rotation - Left and Right

numbers = [1, 2, 3, 4, 5]

print("Original List:", numbers)

k = int(input("Enter rotation positions: "))

k = k % len(numbers)

# Left Rotation
left_rotation = numbers[k:] + numbers[:k]

# Right Rotation
right_rotation = numbers[-k:] + numbers[:-k] if k != 0 else numbers[:]

print("Left Rotation:", left_rotation)
print("Right Rotation:", right_rotation)
