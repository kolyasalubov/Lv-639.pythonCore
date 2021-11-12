class Human:

    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name}")
    
    def just():
        print('Just!')
    
    @classmethod
    def info_species(cls):
        return cls.species

    @staticmethod
    def static_arb():
        return "life is good!"


man = Human("Adam")
woman = Human("Eva")

print(woman.info_species())
print(Human.static_arb())
