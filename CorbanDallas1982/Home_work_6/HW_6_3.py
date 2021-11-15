word = input("Enter your word:")
def f():
    global word
    return {x: list(word).count(x) for x in list(word)}
print(f())