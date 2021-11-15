def filter_words(st):
    st=st.lower().split()
    st[0]=st[0].title()
    st1=' '.join(st)
    return st1