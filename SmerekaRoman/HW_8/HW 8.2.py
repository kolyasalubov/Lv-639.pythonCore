class Human():

    def __init__(self, name):
        self.name = name

    def hello(self):
        return f"Hello {self.name} !"

    @classmethod
    def species(cls):
        h_species = 'Homo sapiens sapiens'
        return h_species, cls

    @staticmethod
    def message():
        return 'well done'

person = Human('Mark')
print(person.hello())
print(person.species())
print(person.message())
