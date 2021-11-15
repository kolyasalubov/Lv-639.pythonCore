class Employee():
    '''This is Home Work 8.3'''
    counter = 0

    def __init__(self, name, salary) -> None:
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def number_of_workers (self):
        return f'Number of workers is {Employee.counter}'

    def worker_info(self):
        print (f'My name is - {self.name}')
        print (f'My salary is - {self.salary} $')

worker_1 = Employee('Ivar', 2000)
worker_1.worker_info()
worker_2 = Employee('Roman', 2300)
worker_2.worker_info()
worker_3 = Employee('Jack', 3000)
worker_3.worker_info

print(worker_3.number_of_workers())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__doc__)


