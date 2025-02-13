
def findNthNumber(number, rank, smallOrlarge):
    if smallOrlarge.upper() == 'small'.upper():
        number.sort()

    if smallOrlarge == 'large':
        number.sort(reverse=True)

    count= 0
    flag= None
    result =1

    for num in number:
        if num==flag:
            pass
        else:
            count +=1
            flag= num
            
        if count== rank:
            return num



print(findNthNumber([7,8,92,1,1,9,6],3,'large'))
