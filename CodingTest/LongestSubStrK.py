#https://www.youtube.com/watch?v=V1gF8FCHz60
#longest substring with k unique characters

def longestSub(st,k):

     l,r=0,0
     seen= {}
     result=0

     while r<len(st):
         if st[r] not in seen:
             k-=1
         seen[st[r]] = r

         while k<0:
             if seen[st[l]]== l:
                del seen[st[l]]
                k +=1
             l +=1

         result = max(result,r-l+1)
         r +=1
     return result

print(longestSub('ecebaa',2))