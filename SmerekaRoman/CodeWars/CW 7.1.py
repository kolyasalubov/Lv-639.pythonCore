def count_positives_sum_negatives(arr):
    pos_counter = [value for value in arr if value >= 1]
    neg_summa = [negative for negative in arr if negative < 1]
    return [len(pos_counter), sum(neg_summa)] if arr else []