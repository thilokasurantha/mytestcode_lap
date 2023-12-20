# a = [9, 17, 30, 38, 39]
# c=0
# d=1
# s=set({})
# while(d<len(a)) :
#     if a[d] == a[c]+1 :
#         print(c, d)
#         s.add(c)
#         s.add(d)
#         c+=1
#         d+=1
#     else :
#         c+=1
#         d+=1
# print(s)

x = "12+3+(4+8)+(80+20)+40+50+((2*4)+(30+40))+((((5*4)+(3+4))))"
y = []
z = []
for i in x :
    y.append(i)
for j in range(0, len(x)-1) :
    z.append(j)

print(y)
print(z)


p = [1.2,3]
q=[2,3]

if q in p :
    p.remove(q)
    print(p)


x = [1,2,3,4,5,[1,3,4]]
y = [1,2,3,4,5,6]
x.remove(y[0])
print(x)