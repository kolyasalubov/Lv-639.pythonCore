def count_sheeps(sheep):
    count=0
    for i in range(len(sheep)):
        if sheep[i]==True:
            count+=1
    return count