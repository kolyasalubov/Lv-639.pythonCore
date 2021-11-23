def reverse(st):
    words = st.split(' ')
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

print(reverse('Hello Word'))
print(reverse('Hi There.'))
