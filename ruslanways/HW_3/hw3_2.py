inputed_number = input("Please type 4-digits number: ")

x = list(inputed_number)

print(x)

summ_of_inputed_number = int(x[0])+int(x[1])+int(x[2])+int(x[3])

print(summ_of_inputed_number)

print(''.join(sorted(inputed_number, reverse=True)))

x.sort()
inputed_number = ''.join(x)
print(inputed_number)
