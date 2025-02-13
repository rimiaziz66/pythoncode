#Question: Given a list of n-1 numbers in the range 1 to n, find the missing number.
def missingNumber(ls):
    n=len(ls)+1

    total=sum(ls)
    nNum= (n*(n+1)//2)-total
    return nNum

print(missingNumber([1,2,3,4,5,7]))