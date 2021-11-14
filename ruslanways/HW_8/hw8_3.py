class Employee():

    """
    class Employee
    """

    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1
    
    def total_employees(self):
        print(f"Total number of employees are {Employee.counter}.")

    def info_employee(self):
        print(f"The employee {self.name} has a salary of {self.salary}$.")

employee1 = Employee("Ruslan", 1200)
employee2 = Employee("Oksana", 2900)
employee3 = Employee("Robert", 1300)
employee4 = Employee("Vasyl", 600)

Employee.total_employees(employee2)
employee3.total_employees()
employee4.info_employee()
employee2.info_employee()

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)
