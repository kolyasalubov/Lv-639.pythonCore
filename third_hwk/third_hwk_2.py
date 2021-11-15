
#First task

initial_value = list(input("Input a number "))
print ("Your number before changes", int("".join(initial_value)))
first_step = list (map (int, initial_value))
print("Sum numbers of input value = ", sum(first_step))

#Second task

first_step.reverse()
first_step = list (map (str, first_step))
print("Our Values after reverse", int("".join(first_step)))

#Third task

first_step.sort()
first_step = list (map (str, first_step))
print("Our Values after sorted", int("".join(first_step)))




