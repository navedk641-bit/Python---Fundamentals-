# Remove Duplicates Without Using Set

numbers = [1, 2, 3, 2, 4, 1, 5, 3]

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Original List:", numbers)
print("List Without Duplicates:", unique_list)
