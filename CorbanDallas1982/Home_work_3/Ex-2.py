n = int(input('Enter a number: '))
print ('Task 2. Reversive write order')
reverse = str(n)
print (reverse[::-1])
print ('')
print ('Task 3. Sorted number')
print (sorted(str(n)))
print ('')
print ('Task 1. Multeply of digits ')
multiply = 1
while n >0:
    digit = n%10
    multiply = multiply*digit
    n = n//10
print('The product of digits is:', multiply)
