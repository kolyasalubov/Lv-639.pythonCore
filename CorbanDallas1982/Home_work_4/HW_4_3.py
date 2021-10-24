f1 = 1
f2 = 1
number = int(input('Enter a number n: '))
print("")
print("The Fibonacci numbers is:")
print("0", f1, f2, end=' ')
for i in range(2, number):
    f1, f2=f2, f1+f2
    print(f2, end=' ')
    
