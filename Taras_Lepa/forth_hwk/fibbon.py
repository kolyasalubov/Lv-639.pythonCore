#fibbon



fib1 = 1
fib2 = 1
fibb_list=[0,1,1]
target = int(input("Values for Fibbonachy way "))
i = 2 

if target < 2:
    print(f"Values for your values : {fib2}")
else:
    while i < target:
        fibb_sum = fib2 + fib1
        fibb_list.append(fibb_sum)
        fib1 = fib2
        fib2 = fibb_sum
        i += 1
 
print (f"Values for your values = {fibb_sum}" )
print(f"Fibb ways : {fibb_list}")
