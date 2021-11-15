def largestNumber(num_1,num_2):
    """Used to return the largest number of two numbers"""
    if num_1 > num_2:
        return num_1
    elif num_1 < num_2:
        return num_2
    else:
        return None
number_1=56
number_2=58
result=largestNumber(number_1,number_2)
print("The largest number is ",end="")
print(result) if result != None else print("not defined. They equal")