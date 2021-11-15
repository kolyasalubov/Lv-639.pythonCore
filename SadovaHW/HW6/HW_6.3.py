user_word=input("Write some word ")
dict={}
for char in user_word:
    dict[char] = user_word.count(char)
    
print(dict)