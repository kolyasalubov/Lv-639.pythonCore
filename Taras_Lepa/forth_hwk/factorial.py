#First work use loop while
user_input=int(input("Give me needed Factorial "))
factorial=1
item=1
if (user_input):
   while  item <= user_input:
      factorial*=item
      item +=1
print(factorial)





user_input = abs(int(input("Give me a number ")))
factorial = 1
if (user_input):
   for i in range(1,user_input + 1):
        factorial*=i
   print(f"Factorial values for yours namber will be equal {factorial}")        
else:
   print(f"Factorial for zero equal {factorial}")