n=int(input())
m=int(input())
d=[]
for _ in range(n):
    a=input()
    b=int(input())
    d.append([a,b])
d=sorted(d,key=lambda x:x[1])
i=0
j=m-1
mi=d[j][1]-d[i][1]
for k in range(1,n-m+1):
    p=d[k+m-1][1]-d[k][1]
    if(p<mi):
        i=k
        j=k+m-1
        mi=p
print('The goodies selected for distribution are:')
for q in range(i,j+1):
    print(*d[q])
print('And the difference between the chosen goodie with highest price and the lowest price is',d[j][1]-d[i][1])