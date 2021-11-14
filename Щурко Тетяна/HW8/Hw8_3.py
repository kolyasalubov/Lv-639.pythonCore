class Employee:
    """An employee class.Has name and salary."""
    counter=0
    def __init__(self, name, salary):
        Employee.counter+=1
        self.name=name
        self.salary=salary
    def get_employees(self):
        return Employee.counter
    def get_employee(self):
        print(f"Name of this employee is {self.name}\n"
              f"Salary is {self.salary}")

James=Employee("James",5600)
James.get_employee()
Lilly=Employee("Lilly",3442)
Lilly.get_employee()
Lesley=Employee("Lesley",3212)
Lesley.get_employee()
Gordon=Employee("Gordon",9878)
Gordon.get_employee()
Amina=Employee("Amina",6574)
Amina.get_employee()
print(f"Count of employees is {Employee.counter}")
print(f"Information about the base classes '{Employee.__base__}'")
print(f"Information about the class namespace '{Employee.__dict__}'")
print(f"Information about the class name '{Employee.__name__}'")
print(f"Information about the module name in which the class defined '{Employee.__module__}'")
print(f"Information about the documentation bar '{Employee.__doc__}'")
