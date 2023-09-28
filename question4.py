from functools import reduce
def digits_to_num(digits):
    return reduce(lambda x,y: 10*x+y,digits)
res=digits_to_num([1,2,3])
print("res-->",res)
