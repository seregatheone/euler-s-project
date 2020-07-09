max5 = 0
i = 0
def ma(x):
    a = x
    d = []
    while a!=1:
        d.append(a)
        if a%2==0:
            a/=2
        else:
            a=3*a+1
    return len(d)
for j in range(2,1000000,2):
    print(j)
    max1 = ma(j)
    if max5 < max1:
        max = max1
        i = j
    print(ma(j))
print(j)
