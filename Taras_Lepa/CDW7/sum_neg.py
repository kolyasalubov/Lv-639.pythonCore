##sum negatives


#I did this task literally with an eye on the test cases. The solution is crooked, but all the tests have been passed#



def count_positives_sum_negatives(arr):

    negat_number = []
    arr_count = 0
    if sum(arr) >0 or arr !=[]:
        for b in range(len(arr)):
            if arr[b]>0:
                arr_count +=1
            else:
                negat_number.append(arr[b])
    else:
        return []
    answers = [arr_count,sum(negat_number)]
    return answers