def charcalc(text):
    calc = {}
    for n in text:
        keys = calc.keys()
        if n in keys:
            calc[n] += 1
        else:
            calc[n] = 1
    return calc

print("""
********************************** Hello! **********************************
This program can calculate the number of characters included in a given text
****************************************************************************""")

words = input("\nEnter your text here: ")
print(charcalc(words))