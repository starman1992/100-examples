i,j,x = 0,1,0
while (i < 5) :
    x = 4 * j
    for i in range(0,5) :
        if(x%4 != 0) :
            break
        else :
            i += 1
        x = (x/4) * 5 +1
    j += 1
print(x)

##第5只猴分的5份其中每份1个，且多一个，共6个
##共有5次判断，每次都是判断剩下的桃子数量减一后是否可以除尽5？
##办法是引入count作为计数器，满足以上条件一次则count-1，直至count=0；
##如果中间有无法除尽的情况(num - 1) % 5 != 0，则程序跳出判断，返回-1值
##
##需要思考每次猴子连吃带拿，剩下的桃子数量变动是否符合递归？
##每一次分配桃子都有共同的地方：减去1，再除以5，可以除尽
##符合递归的特征：
##描述第count次分桃子和第count-1次分桃子，桃子数量num之间存在以下联系
##num = (num - 1) * 4 / 5
##只有当if判断num能整除5，则输出下一个猴子分桃时看到的桃子数量
##return consume(count - 1, num)

def consume(count, num):
    if count == 0:
        return 1
    elif (num - 1) % 5 == 0:
        num = (num - 1) * 4 / 5
        return consume(count - 1, num)

count = int(input('请输入猴子个数：'))
num = 1
while count:
    num+=1
    if consume(count,num) == 1:
        print('原来最少有 %d 个桃子'%num)
        break
