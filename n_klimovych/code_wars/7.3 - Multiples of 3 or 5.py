def solution(number):
    numb = []
    for i in range (number):
        if i % 3 == 0 or i % 5 == 0:
            numb.append(i)
    nsum = sum(numb)
    return nsum