#输出第n个斐波那契数
def Fib(n):
    return 1 if n<=2 else Fib(n-1)+Fib(n-2)
print(Fib(int(input())))
    
res,a,b=0,1,1
for i in range(num-1):
    a,b=b,a+b
print(a)

#建成列表
def fib(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs
# 输出前 10 个斐波那契数列
print(fib(num))

month=int(input('繁殖几个月？： '))
month_0,month_1,month_elder=1,0,0
for i in range(month):
    month_0,month_1,month_elder=month_elder+month_1,month_0,month_elder+month_1
    print('第%d月末共'%(i+1),month_0+month_1+month_elder,'对兔子')
    print('新生兔：',month_0,end='   ')
    print('1月兔：',month_1,end='   ')
    print('2月兔：',month_elder)
