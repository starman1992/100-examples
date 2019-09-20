import time
#输出当前时间
for i in range(4):
    print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
    time.sleep(1)

#暂停1秒输出
for i in range(4):
    print(str(int(time.time()))[-2:])
    time.sleep(1)

