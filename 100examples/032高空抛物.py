n=int(input('请输入要计算的次数:'))
height=100
tour = []

def tour_sum(num):
    long = height
    for i in range(num):
        tour.append(long)
        long /= 2
        tour.append(long)
    print('第%d次回弹高度是%f米' % (num,long))
    return sum(tour)-long
print('第%d次落地时共走路程%f米'% (n,tour_sum(n)))
