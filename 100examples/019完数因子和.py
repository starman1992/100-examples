def factor(num):
    target=int(num)
    res={1}
    for i in range(2,num):
        if num%i==0:
            res.add(i)
##            res.add(num/i)
    return res

for i in range(2,1001):
    if i==sum(factor(i)):
        print(i,factor(i))
