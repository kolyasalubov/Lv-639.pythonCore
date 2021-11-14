print ('1 - rectangle')
print ('2 - triangle')
print ('3 - circle ')
d = int(input('Select a figure: '))
def f1(x, y):
    return x*y
def f2(x,y,z,k):
    return (k*(k-x)*(k-y)*(k-z))**0.5
def f3(x):
    return 3.14*x**2
if d == 1:
    print ('The calculation of area of rectangle')
    a = int(input('Enter a lenght of side a (m.): '))
    b = int(input('Enter a lenght of side b (m.): '))
    print ('The area of rectangle is',f1(a,b), 'm.')
elif d == 2:
    print ('The calculation of area of a triangle')
    a = int(input('Enter a lenght of side a (m.): '))
    b = int(input('Enter a lenght of side b (m.): '))
    c = int(input('Enter a lenght of side c (m.): '))
    p = (a+b+c)/2
    print ('The area of rectangle is', f2(a,b,c,p), 'm.')
else: 
    print ('The calculation of area of a circle.')
    a = int(input('Enter a radius of circle (m.): '))
    print ('The area of rectangle is', f3(a), 'm.')