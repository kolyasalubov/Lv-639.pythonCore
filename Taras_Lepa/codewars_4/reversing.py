def reverse(st):
    st = " ".join(reversed(st.split())).strip()
    return st
    

reverse("Hello world i am here")