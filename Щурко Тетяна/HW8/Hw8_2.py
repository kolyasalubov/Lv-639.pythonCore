class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome {self.name}!!!")

    @classmethod
    def return_species(cls):
        return cls.species

    @staticmethod
    def arbitraty_message():
        message=input(f"Enter your message = ")
        print(f"Message is {message}")

Maria = Human("Maria")
Maria.welcome_message()
print(f"{Maria.name}s species is", Maria.return_species())
Maria.arbitraty_message()
