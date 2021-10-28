# last_number=int(input("Enter last number="))
# while  < last_number

def fibonacci(max):  # генератор (а не функция, т.к. оператор return заменён на yield)
    a, b = 0, 1
    while a < max:
        yield a  # return a, + запоминаем место рестарта для следующего вызова
        a, b = b, a + b  # параллельное присваивание, которое выполняется одновременно и параллельно


for n in fibonacci(1000):  # используем генератор fibonacci() как итератор
    print (n),  # печатаем все числа Фибоначчи меньшие 100 через пробел