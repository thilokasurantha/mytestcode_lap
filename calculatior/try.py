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


p = [[2,3],[4,5]]
del p[0][1]
print(p)
p[0].append(p[1][0])
print(p)