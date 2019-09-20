import time
import random

I=[]
i=0
play_it = input('你想玩猜数字游戏吗.(Y or N)：')
while play_it in ['Y','y']:
    c = input('输入你的角色:')
    I.append([c])
    x = random.randint(1,101)
    start = time.perf_counter()
    guess = int(input('请输入你猜的数字:\n'))
    I[i].append(guess)
    while guess != x:
        if guess > x:
            print('再小一点！')
            guess = int(input('请输入你猜的数字:\n'))
            I[i].append(guess)
        elif guess < x:
            print('再大一点！')
            guess = int(input('请输入你猜的数字:\n'))
            I[i].append(guess)
        else:
            guess = int(input('你输入的数字是?'))
            I[i].append(guess)
    end = time.perf_counter()
    print ('你花了 %.2f 秒猜到了数字 %d.' % (end-start,x))    
    if end-start < 15:
        print ('真聪明!')
    elif end-start < 25:
        print ('还可以再快一点点!')
    else:
        print ('继续努力吧!')
    print ('%s ,你猜过的数字有 %s, 猜每个数字用了 %.2f 秒'% \
           (c,I[i][1:],(end-start)/(len(I[i])-1)))
    play_it = input('do you want to play it again.')
    i += 1        
        
