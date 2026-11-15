# Check Whether One Set Is a Subset of Another

set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

print("First Set:", set1)
print("Second Set:", set2)

if set1.issubset(set2):
    print("Set1 is a subset of Set2")
else:
    print("Set1 is not a subset of Set2")
