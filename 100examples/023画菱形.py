def draw(num):
    for i in range(1,num*2,2):
        a=i*'*'
        print(a.center(2*num+1,' '))
    for i in range(2*num-3,0,-2):
        a=i*'*'
        print(a.center(2*num+1,' '))
draw(10)
