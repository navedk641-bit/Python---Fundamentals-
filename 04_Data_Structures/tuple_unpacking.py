# Swap First and Last Elements Using Tuple Unpacking

numbers = (10, 20, 30, 40, 50)

print("Original Tuple:", numbers)

# Swap first and last elements
first, *middle, last = numbers

swapped_tuple = (last, *middle, first)

print("Tuple After Swapping:", swapped_tuple)
