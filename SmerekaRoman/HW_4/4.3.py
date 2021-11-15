limit_number = int(input("Please input the number: "))
fibonacci = [0,1]
while fibonacci[-1] < limit_number:
    if (fibonacci[-1]+fibonacci[-2]) >= limit_number:
        break      
    fibonacci.append(fibonacci[-1]+fibonacci[-2])
print(fibonacci)