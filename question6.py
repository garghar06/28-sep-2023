def concatenate(L1,L2,connector):
    return [x+connector+y for x,y in zip(L1,L2)]
res=concatenate(['A','B'],['a','b'],'-')
print("res-->",res)