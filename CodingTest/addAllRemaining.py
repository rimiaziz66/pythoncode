
def addAllRemaining(ls):
    n=len(ls)
    prefix= 0
    suffix=0
    result= [0]* n

    for i in range(n):
        result[i] = prefix
        prefix += ls[i]

    for j in range(n-1,-1,-1):
        result[j] += suffix
        suffix += ls[j]

    return result

ls= [3,1,5,3]

a= addAllRemaining(ls)
print(a)


