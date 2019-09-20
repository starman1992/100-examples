##target=int(input('输入一个整数：'))
##print(target,'= ',end='')
##
##flag=0
##while True:
##    if flag:
##        break
##    for i in range(2,int(target+1)):
##        if target % i == 0:
##            print("%d" % i,end='')
##            if target == i:
##                flag = 1
##                break
##            print('*',end='')
##            target /= i
##            break
        
##I=[]
##n = int(input('请输入数字：'))
##def min_yueshu(m):
##    if m>1:
##        for i in range(2,m+1):
##            if m % i == 0:
##                I.append(i)
##                I.append('*')
##                min_yueshu(int(m/i))
##                break
##    else:
##        del I[-1]   
##min_yueshu(n)
##print('%d=' % n,end='')
##[print(I[i],end='') for i in range(len(I))]

I=[]
n = int(input('请输入数字：'))
print('%d=' % n,end='')
while n-1:
    if n>1:
        for i in range(2,int(n+1)):
            if n % i == 0:
                I.append(i)
                I.append('*')
                n /= i
                break
del I[-1]   
[print(I[i],end='') for i in range(len(I))]
