def singlenumber(array):
    
    res=0
    for i in array:
        res=i^res
    return res

array=list(map(int,input().split()))
print(singlenumber(array))