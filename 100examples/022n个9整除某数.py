zi = int(input('输入一个数字:'))
n1 = 1
c9 = 1
m9 = 9
sum = 9
while n1 != 0:
    if sum % zi == 0:
        n1 = 0
    else:
        m9 *= 10
        sum += m9
        c9 += 1
print ('%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum))
r = sum / zi
print ('%d / %d = %d' % (sum,zi,r))

x=int(input('输入一个数字:'))
n=0
a=9
while n<10000:
    n+=1
    if a%x == 0:
        print(a,len(str(a),'个9可以整除','x'))
        break
    else:
        a=a*10+9
