def list_animals(animals):
    my_list = ''
    k=1
    for i in animals:
        my_list += f"{k}. {i}\n"
        k+=1
    return my_list
