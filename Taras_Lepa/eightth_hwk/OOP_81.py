###Employee OOP p 81


class Employee():

    '''
    Now we will do a Employee class.Object of this class will have
    name,salary and others.
    '''
    
    count_worker=0
    

    def __init__(self,name,salary):
        self.salary = salary
        self.name = name
        Employee.count_worker +=1

    def print_info(self):
        print(f"{self.name} is worker ,{self.salary} his salary")

    def number_of_workers (self):
        message = f'Number of workers is {Employee.count_worker}'
        return message
    
tom = Employee("Tom",36000)
tom.print_info()

print(tom.number_of_workers())

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__doc__)
print(Employee.__module__)
print(Employee.__name__)

