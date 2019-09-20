##
res=1
def 
for i in range(4,1,-1):
    res=i*res+1
    print(i,res)
print(res)
##
def jc(n):
    return n * jc(n-1) if n>1 else 1
res=0
for i in range(4):
    res += jc(i+1)
print(res)
##
n,s,t = 0,0,1
for n in range(1,21):
    t *= n
    s += t
print (s)
##
s = 0
l = range(1,21)
def op(x):
    r = 1
    for i in range(1,x + 1):
        r *= i
    return r
print(sum(map(op,l)))
