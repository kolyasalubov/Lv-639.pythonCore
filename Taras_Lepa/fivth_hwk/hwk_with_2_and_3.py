len_array = int(input("Input values "))
spisok = list(range(len_array))
det_on_2_and_3 = []
det_on_2 = []
det_3 = []
natural_number = []
for i in spisok:
    if (spisok[i]%2 ==0 and spisok[i] % 3  ==0 ):
        det_on_2_and_3.append(i)
        det_on_2.append(i)
        det_3.append(i)
    elif (spisok[i]%2 ==0):
        det_on_2.append(i)
    elif (spisok[i]%3 ==0):
        det_3.append(i)
    else :
        natural_number.append(i)
        
print(det_on_2_and_3)
print(det_on_2)
print(det_3)
print(natural_number)
