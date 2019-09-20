for i in range(100,1000):
    s=str(i)
    one=int(s[-1])
    ten=int(s[-2])
    hun=int(s[-3])
    if i == one**3+ten**3+hun**3:
        print(i)

for i in range(100,1000):
    if i == (i//100)**3+((i%100)//10)**3+(i%100%10)**3:
        print(i)


def Narcissus():
    for each in range(100,1000):
        temp = each
        sum = 0
        while temp:
            sum = sum + (temp%10)**3
            temp = temp // 10

        if sum == each:
            print(each,end = '\t')

print('所有水仙花数分别是：',end = '\n')
Narcissus()
