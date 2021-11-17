class Employee():
    
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    
    def all_employees(self):
        print(f"The all employees are {Employee.counter}.")

    def info_employee(self):
        print(f"The employee {self.name} has a salary {self.salary} $.")

employee_1 = Employee("Jack", 2500)
employee_2 = Employee("Emma", 2300)
employee_3 = Employee("Andy", 2800)

Employee.all_employees(employee_1)
employee_3.all_employees()
employee_2.info_employee()

print(Employee.__base__)
print(Employee.__name__)
print(Employee.__dict__)
print(Employee.__module__)
print(Employee.__doc__)