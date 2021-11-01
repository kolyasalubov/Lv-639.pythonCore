def largest_1 (a = int,b = int):
    '''a: integer
       b: integer'''
    if a > b:
        return f"The largest number is {a}"
    else:
        return f"The largest number is {b}"

number = largest_1(142, 235)
print(number)