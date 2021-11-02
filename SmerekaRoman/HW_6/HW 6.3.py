def numb_of_char(a):
    d = {}
    for char in set(a):
        d[char] = a.count(char)
    return d

a = numb_of_char(str(input("Input the word please: ")))
print(a)

