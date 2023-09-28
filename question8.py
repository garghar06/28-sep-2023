def count_match_index(L):
    return len(list(filter(lambda x:x[0]==x[1], [pair for pair in enumerate(L)])))
res=count_match_index([0,2,2,1,5,5,6,10])
print("res-->",res)