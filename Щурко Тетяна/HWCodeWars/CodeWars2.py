def reverse(st):
    st = st.split(' ')
    st=st[::-1]
    st_1=[]
    for i in range(len(st)):
        if st[i]!='':
            st_1.append(st[i])
    st_1=' '.join(st_1)
    return st_1