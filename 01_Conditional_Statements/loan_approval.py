# Loan Approval System

salary = float(input("Enter your monthly salary: "))
credit_score = int(input("Enter your credit score: "))
age = int(input("Enter your age: "))

if salary >= 30000 and credit_score >= 700 and 21 <= age <= 60:
    print("Loan Status: APPROVED")

elif (salary >= 30000) + (credit_score >= 700) + (21 <= age <= 60) == 2:
    print("Loan Status: CONDITIONALLY APPROVED")

else:
    print("Loan Status: REJECTED")
