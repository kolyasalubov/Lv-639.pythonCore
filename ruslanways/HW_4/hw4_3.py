n = int(input("\nPlease enter integer number: "))
k1 = 0
k2 = 1
k = 0
print("Here are Fibonacci numbers:", end=" ")

print(k1, end=", ")
print(k2, end="")

while k < n:
    k = k1 + k2
    if k >= n:
        print('.\n')
        break
    print(f", {k}", end="")
    k1 = k - k1
    k2 = k
    