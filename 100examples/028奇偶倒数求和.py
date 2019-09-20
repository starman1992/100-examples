def peven(n):
    i = 0
    s = 0.0
    for i in range(2,n + 1,2):
        s += 1.0 / i
    return s
def podd(n):
    s = 0.0
    for i in range(1, n + 1,2):
        s += 1.0 / i
    return s
def dcall(fp,n):
    s = fp(n)
    return s
n = int(input('input a number: '))
if n % 2 == 0:
    sum = dcall(peven,n)
else:
    sum = dcall(podd,n)
print (sum)

def hs(num):
    s=0
    if num%2==0:
        for i in range(2,num+1,2):
            s += 1/i
    else:
        for i in range(1,num+1,2):
            s += 1/i
    return s
n = int(input('input a number: '))
print(hs(n))
