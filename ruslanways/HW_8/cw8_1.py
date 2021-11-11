def summation(num):
    if num == 1:
        return 1
    else:
        num+=summation(num-1)
        return num

print(summation(4))
