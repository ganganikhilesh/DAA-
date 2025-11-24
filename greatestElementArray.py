a=[2,2,1,1,2,2]
b=[a[0]]
c=[1]
for i in range(len(a)):
    for j in range(len(b)):
        if (a[i]==b[j]):
            c[j]+=1
            break
        elif(a[i]!=b[j] and j==len(b)-1):
            c.append(1)
            b.append(a[i])
c[0]-=1
d=0
for i in range(len(b)):
    if(c[i]>d and c[i]>(len(a)/2)):
        d=b[i]
print(d)