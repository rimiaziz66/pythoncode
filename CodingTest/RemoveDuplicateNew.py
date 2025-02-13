
def remove_duplicate(ls):
    result = set()
    a={result.add(l) for l in ls if l not in result}
    return a
ls=[3,4,6,2,3,5,4]
a=remove_duplicate(ls)
print(a)