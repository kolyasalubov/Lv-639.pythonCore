def calc_of_char(your_string):
    num_of_char = {}
    for letter in your_string:
        if letter == ' ':
            continue
        else:
            num_of_char[letter] = your_string.count(letter)
    return num_of_char

print(calc_of_char(input('Please, enter your sentence or word ')))