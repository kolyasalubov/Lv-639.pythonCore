class Employee:

    num_of_empl = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.num_of_empl += 1
    
    def workers_number(self):
        return f'{Employee.num_of_empl} is the overall number of workers.'

    def worker_info(self):
        return f'{self.name} works here. His salary is {self.salary}'

tom = Employee('Tom', 1500)
tom.worker_info()
andy = Employee('Andy', 5000)
andy.worker_info()
sarah = Employee('Sarah', 2900)
sarah.worker_info()
kevin = Employee('Kevin', 9000)
kevin.worker_info()

print(Employee.workers_number(tom))
print(Employee.__doc__)
print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)


