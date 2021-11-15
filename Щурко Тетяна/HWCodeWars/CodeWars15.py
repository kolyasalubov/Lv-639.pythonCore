def solution(number):
    summ = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            summ += i
    return summ
