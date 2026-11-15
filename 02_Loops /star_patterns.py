# Different Star Patterns

rows = 5

# 1. Right Triangle
print("Right Triangle")

for i in range(1, rows + 1):
    print("* " * i)

# 2. Pyramid
print("\nPyramid")

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# 3. Diamond
print("\nDiamond")

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * (2 * i - 1))

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * (2 * i - 1))
