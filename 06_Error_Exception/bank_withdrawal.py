try:
    balance = float(input("Enter account balance: "))
    amount = float(input("Enter withdrawal amount: "))

    if amount > balance:
        raise Exception("Insufficient balance!")

    balance = balance - amount

    print("Withdrawal successful.")
    print("Remaining balance:", balance)

except Exception as e:
    print("Error:", e)
