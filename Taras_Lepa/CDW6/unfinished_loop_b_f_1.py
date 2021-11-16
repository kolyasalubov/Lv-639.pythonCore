#unfinished_loop create array



def create_array(n):
    res=[]
    i=1
    while len(res)<=n: 
        res.append(i)
        i+=1
        if len(res)== n:
            break
    return res

