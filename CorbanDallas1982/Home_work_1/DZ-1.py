name = input ("What is your name? ")
try:
    age = int(input('How old are you? '))
except ValueError:
    print ("You cant enter letters, you must must enter just numbers")
    age = int(input('How old are you? '))
lok = input('Where do you live? ')
print ("Hello," , name)
print ("Your age is: " , age)
print ("You live in: " , lok)
