fibo_1 = 0
fibo_2 = 1
 
number = int(input("Please enter the number "))
 
print(fibo_1, fibo_2, end=' ')
 
for i in range(2, number):
    fibo_1, fibo_2 = fibo_2, fibo_1 + fibo_2
    print(fibo_2, end=' ')