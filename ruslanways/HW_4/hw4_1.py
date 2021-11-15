inputed_number = int(input("Please type integer number: "))

if inputed_number == 0:
    print(f"Factorial '{inputed_number}' is: 1")

elif inputed_number <0:
    print("There is no factorial's value of a negative number!")

else: 
    str1 = list(range(1, inputed_number+1))
    n = 0
    while n < len(str1):
        if n == 0:
            str1[n] = str(str1[n])
        else:
            str1[n] = "*" + str(str1[n])
        n+=1   

    x = eval("".join(str1))

    print(f"Factorial '{inputed_number}' is: {x}")
