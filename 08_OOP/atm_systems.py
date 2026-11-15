class ATM:
    def _init_(self, pin, balance):
        self.__pin = pin
        self.__balance = balance

    def check_pin(self, pin):
        return self.__pin == pin

    def check_balance(self, pin):
        if self.check_pin(pin):
            print("Balance:", self.__balance)
        else:
            print("Incorrect PIN")

    def withdraw(self, pin, amount):
        if not self.check_pin(pin):
            print("Incorrect PIN")
        elif amount <= 0:
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient Balance")
        else:
            self.__balance -= amount
            print("Withdrawal Successful")
            print("Remaining Balance:", self.__balance)


atm = ATM(1234, 5000)

pin = int(input("Enter PIN: "))

atm.check_balance(pin)

amount = int(input("Enter withdrawal amount: "))
atm.withdraw(pin, amount)
