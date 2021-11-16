#loop animals with mistake


def list_animals(animals):
    animals_list = ''
    for i in range(len(animals)):
        animals_list += str(i + 1) + '. ' + animals[i] + '\n'
    return animals_list


list_animals(["dog","duck","frog"])

