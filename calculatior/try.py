a = [9, 17, 30, 38, 39]
c=0
d=1
s=set({})
while(d<len(a)) :
    if a[d] == a[c]+1 :
        print(c, d)
        s.add(c)
        s.add(d)
        c+=1
        d+=1
    else :
        c+=1
        d+=1
print(s)
