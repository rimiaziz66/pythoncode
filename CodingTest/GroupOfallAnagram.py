#alist = ["abd", "dbf", "adb", "fdb"]

from collections import defaultdict
def groupAnagram(alist):

    adic = defaultdict(list)

    for l in alist:
        k= tuple(sorted(l))
        adic[k].append(l)

    nlist=[]
    for v in adic.values():
        nlist.append(v)

    return nlist

alist = ["abd", "dbf", "adb", "fdb"]
a= groupAnagram(alist)
print(a)

