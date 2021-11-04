def count_positives_sum_negatives(arr):
    result=[0]*2
    for i in arr:
        if i < 0:
            result[1] += i
        elif i > 0:
            result[0] += 1
    return result