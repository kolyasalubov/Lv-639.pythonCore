number_to_fuctorial=int(input("Enter number, factorial of which we should find = "))
factorial=1
while(number_to_fuctorial>0):
    factorial*=number_to_fuctorial
    number_to_fuctorial-=1
print(factorial)