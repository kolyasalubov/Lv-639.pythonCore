var_1=int(input('Enter first variable:'))
var_2=int(input('Enter second variable:'))
print(f"First variable {var_1}, second variable {var_2}")
var_1,var_2=var_2,var_1
print(f"After change: The first variable is {var_1} and the second variable is {var_2}")