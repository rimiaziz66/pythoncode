# Merge 2 sorted list into one sorted list
def merge2list(ls1,ls2):
    ln1= len(ls1)
    ln2= len(ls2)
    i,j= 0,0
    nls = []
    while i<ln1 and j<ln2:
        if ls1[i]<ls2[j]:
            nls.append(ls1[i])
            i +=1
        else:
            nls.append(ls2[j])
            j +=1
    while i<ln1:
        nls.append(ls1[i])
        i +=1
    while i<ln2:
        nls.append(ls2[j])
        j+=1
    return nls

ls1=[5,6,7,8]
ls2=[1,2,4,6 ]
print(merge2list(ls1,ls2))