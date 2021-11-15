a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))

print(f"Before swapping: {a} | {b}")
# 1st version:
# a = a + b
# b = a - b
# a = a - b

# 2nd version:
a,b = b,a

print(f"After swapping: {a} | {b}")
input()
