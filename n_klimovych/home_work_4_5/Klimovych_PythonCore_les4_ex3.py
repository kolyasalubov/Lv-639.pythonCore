a, b = 0, 1
c = 0

user_number = int(input("Enter the number of elements in Fibonacci sequence: "))

if user_number <= 0:
    print("Please ententer positive integer")
elif user_number == 1:
    print(f"Fibonacci sequence up to {user_number} looks like this: {a}")
else:
    print("Fibonacci sequence:")
    while c < user_number:
        print(a)
        fib_number = a + b
        a = b
        b = fib_number
        c += 1
input()