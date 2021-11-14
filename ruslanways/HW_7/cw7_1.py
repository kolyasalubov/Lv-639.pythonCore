def count_positives_sum_negatives(arr):
    
    positive = [i for i in arr if i>0]
    negative = [i for i in arr if i<0]

    # print(positive)
    # print(negative)

    # if arr:
    #     return [len(positive), sum(negative)] 
    # else:
    #     return []

    return [len(positive), sum(negative)] if arr else []

print(count_positives_sum_negatives([])) 
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))
