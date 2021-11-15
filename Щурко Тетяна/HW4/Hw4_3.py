number_of_finish=int(input("Enter your number of numbers = "))
fibonachi=[0,1]
i=1
while(sum(fibonachi)<number_of_finish-fibonachi[i]):
    fibonachi.append(fibonachi[i]+fibonachi[i-1])
    i+=1
print(fibonachi)