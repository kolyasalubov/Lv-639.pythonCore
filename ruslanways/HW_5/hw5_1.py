even_divisible_by_2 = [k for k in range(1,11) if k%2==0]
print(even_divisible_by_2)

odd_divisible_by_3 = [k for k in range(1,11) if k%2!=0 and k%3==0]
print(odd_divisible_by_3)

numbers_not_divisible_by_2_and_3 = [k for k in range(1,11) if k%2!=0 and k%3!=0]
print(numbers_not_divisible_by_2_and_3)
