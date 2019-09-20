nmax = 50
n = int(input('请输入总人数:'))
num = []
for i in range(n):
    num.append(i + 1)  
i,k,m = 0,0,0
while m < n - 1:   #m为删除的人数，n为总人数，k是步数，i是座位号
    if num[i] != 0 : k += 1
    if k == 3:
        num[i] = 0
        k = 0
        m += 1
    i += 1
    if i == n : i = 0
print('座位号是 %s 的人留到了最后'%sum(num))


m,n=input('请输入人数和喊点数：').split(',')
m,n=int(m),int(n)
li=list(range(1,m+1))
count = 0
for i in range(1,(m-1)*n+1):
    count+=1
    if i%n==0:
        del (li[count-1])
##        print(li)
        count-=1 
    if count==len(li):
        count=0
print('座位号是 %s 的人留到了最后'%li[0])
