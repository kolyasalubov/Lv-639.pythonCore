#Mutiples of 3 or 5

def solution(number):
    test =" "
    target_list =[]
    if number<=0:
        return 0
    else:
        test = list(range(0,number))
    for i in range(len(test)):
            if i%3 ==0 or i%5 ==0:
               target_list.append(i)
            else:
               continue 
    return sum(target_list)