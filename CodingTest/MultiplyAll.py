
def multiplyAll(ls):
    n=len(ls)
    prefix= 1
    suffix=1
    result= [1]* n

    for i in range(n):
        result[i] = prefix
        prefix *= ls[i]

    for j in range(n-1,-1,-1):
        result[j] *= suffix
        suffix *= ls[j]

    return result

ls= [3,1,5,3]

a= multiplyAll(ls)
print(a)


