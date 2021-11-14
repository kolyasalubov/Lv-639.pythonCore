def largest_numbering(n1, n2):
    """
    function name:  largest_numbering
    parameters:     int, float
    return:         largest number of two inputed numbers
    """
    return n1 if n1>n2 else n2

my_numbers = largest_numbering(9, 8)

print(my_numbers)
