def count_positives_sum_negatives(arr):
    pos, neg = 0, 0
    for i in arr:
        if i > 0: pos += 1
        elif i < 0: neg += i
    return [pos, neg] if arr else []