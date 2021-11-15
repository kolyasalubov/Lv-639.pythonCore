string = input("Enter your sentence = ")
dict={}
for letter in string:
    if letter not in dict:
        dict[letter]=string.count(letter)
print(dict)