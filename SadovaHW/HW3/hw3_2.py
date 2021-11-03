user_number=input("Enter 4-digit number: ")
new_number=list(user_number)

number_sum=int(new_number[0])+int(new_number[1])+int(new_number[2])+int(new_number[3])
reverse_number=new_number[::-1]
sort_number=sorted(new_number)

print(f"Sum of numbers is {number_sum}")
print(f"Reverse numbers is {reverse_number}")
print(f"Sorted numbers is {sort_number}")
