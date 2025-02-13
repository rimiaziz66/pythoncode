# finf longest substring with k unique character


def longestSubStr(st,k):

    charset= set();
    l= 0
    for r in range (len(st)):
        if st[r] in charset:
            charset.remove(st[l])
            k -= 1

