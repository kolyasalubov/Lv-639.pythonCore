#Floating loop

first_list = list(range(10))
for i in first_list:
    first_list[i] = float(first_list[i])
print(first_list)  
