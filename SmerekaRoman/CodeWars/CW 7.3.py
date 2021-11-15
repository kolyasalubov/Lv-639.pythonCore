def solution(number):
    return sum(value for value in range(number) if value % 3 == 0 or value % 5 == 0)