# Exam Result Analyzer

marks = []

for i in range(1, 6):
    mark = float(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

total = sum(marks)
percentage = total / 5

print("\n----- Exam Result -----")
print("Total Marks:", total)
print("Percentage:", percentage, "%")

if any(mark < 33 for mark in marks):
    print("Result: FAIL")

elif percentage >= 60:
    print("Division: First Division")

elif percentage >= 50:
    print("Division: Second Division")

elif percentage >= 40:
    print("Division: Third Division")

else:
    print("Result: FAIL")
