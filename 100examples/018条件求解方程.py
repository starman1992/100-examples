a = 809
for i in range(10,100):
    b = i * a
    if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
        print(i,b)

for i in range(10,100):
    if 8*i>99 or 9*i<100:
        continue
    if 809*i==800*i+9*i:
        print(i,809*i)
        break
x=10
while x<100:
    x+=1
    if len(str(809*x))==4 and len(str(8*x))==2 and len(str(9*x))==3:
        print(x,809*x)
