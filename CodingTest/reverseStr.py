s= " My name is tanvin"

s= s.split()

str =  [ch[: : -1] for ch in s ]
output = ' '.join(str)


st1 = "tanvin"
s1=""

for i in range(len(st1)-1 , -1, -1):
    s1=s1+st1[i]

print(s1)

st2= "My name is Zanyah"
s2 = ""
i = len(st2)-1
while i>=0:
    s2=s2+st2[i]
    i -=1

print (s2)


st3= "My name is sony"
s3 = st3.split()
out3=s3[::-1]
out3=" ".join(out3)
print(out3)

