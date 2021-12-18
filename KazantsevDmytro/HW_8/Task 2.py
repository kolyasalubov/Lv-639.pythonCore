class Human:

    species = 'Homosapiens'

    def __init__(self, name = 'Andy'):
        self.name = name

    def welcome_message(self):
        print("Welcome %s." % (self.name))

    @classmethod
    def the_species(cls):
        return cls.species

    @staticmethod
    def arbitraty_message():
        message = input(f"Enter your message: \n")
        print(f"The message is:\
        \n{message}")

johnny = Human('Johnny')
johnny.welcome_message()
print(f'{johnny.name} is {johnny.the_species()}')
johnny.arbitraty_message()

