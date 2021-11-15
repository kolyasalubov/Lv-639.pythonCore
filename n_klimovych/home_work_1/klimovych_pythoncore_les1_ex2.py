a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
variables = ['+', '-', '*', '**', '/', '//', '%']

print(f"A list of variables: {variables}")
variable = input("\nChoose a variable: ")

if variable == '+':
    c = a + b
elif variable == '-':
    c = a - b
elif variable == '*':
    c = a * b
elif variable == '**':
    c = a ** b
elif variable == '/':
    c = a / b
elif variable == '//':
    c = a // b
elif variable == '%':
    c = a % b
else:
    c = 'Error!'
    print(f"\nYou choose a wrong variable!")
print(f"{a} {variable} {b} = {c}")
input()
