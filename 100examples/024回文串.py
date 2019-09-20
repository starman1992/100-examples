n=input("随便你输入啥啦：")
a=0
b=len(n)-1
flag=True
while a<b:
    if n[a]!=n[b]:
        print('不是回文串')
        flag=False
        break
    a,b=a+1,b-1
if flag:
    print('是回文串')

str = input('请输入文字：')
abc = list(str)
abc1 = list(reversed(abc))
if abc == abc1:
    print(str,'是回文联')
else:
    print(str,'不是回文联')

str = input('请输入文字：')
if str == str[::-1]:
    print(str,'是回文联')
else:
    print(str,'不是回文联')
