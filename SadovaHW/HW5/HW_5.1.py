even_number=[]
odd_number=[]
another_number=[]

for number in range(0,10):
    number+=1
    if number % 2 ==0:
        even_number.append(number)
    elif number % 3 ==0:
        odd_number.append(number)
    else:
        another_number.append(number)
               
print(f"Even numbers are : {even_number}")
print(f"Odd numbers are : {odd_number}")
print(f"Another numbers that not divisible by 2 and 3: {another_number}")