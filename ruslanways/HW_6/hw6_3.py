def calculate_characters(word):
    return {x: list(word).count(x) for x in list(word)}

my_word = calculate_characters('abracadabra')

print(my_word)

