class Human:
    def __init__(self, name):
        self.name = name
        self.species = "Homosapiens"
    def welcome_message(self):
        print(f"Welcome {self.name}!!!")
    def return_species(self):
        return self.species
    def arbitraty_message(self):
        message=input(f"Enter your message to {self.name} = ")
        print(f"Message is {message}")

Maria = Human("Maria")
Maria.welcome_message()
print(f"{Maria.name}s species is", Maria.return_species())
Maria.arbitraty_message()