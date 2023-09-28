def d_list(L):
    dic={}
    for item,val in enumerate(L):
        dic[val]=item
    return dic
res=d_list(['a','b','c'])
print("res-->",res)