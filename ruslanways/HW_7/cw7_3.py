def solution(number):
    
    if number != 0:
        seeking_list = [i for i in range(1, number) if i%3==0 or i%5==0]
        return sum(seeking_list)
    else:
        return 0
