class Human():
    specifies = "Homosapiense"
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Hello, {self.name}"

    @classmethod
    def species(cls):
        h_species = 'Homo sapiens sapiens'
        return f"{cls} is {h_species}"


    @staticmethod
    def any_message():
        message = "Any message"
        return message




bob = Human("Bob")
print(bob.welcome_message())
print(bob.species())
print(bob.any_message())