class Employee:
    def _init_(self, salary):
        self.__salary = salary

    def display_salary(self):
        print("Employee Salary:", self.__salary)


emp = Employee(30000)

emp.display_salary()
