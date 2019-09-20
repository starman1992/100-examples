##def isLeapYear(y):
##    return (y%400==0 or (y%4==0 and y%100!=0))
##DofM=[0,31,28,31,30,31,30,31,31,30,31,30]
##res=0
##year=int(input('Year:'))
##month=int(input('Month:'))
##day=int(input('day:'))
##if isLeapYear(year):
##    DofM[2]+=1
##for i in range(month):
##    res+=DofM[i]
##print(res+day)


import datetime

f = input('请输入年月日（格式：YYYY-MM-DD）:')
yy,mm,dd = f.split('-')
d=datetime.date(int(yy),int(mm),int(dd))
d0=datetime.date(int(yy),1,1)
delta = d-d0+datetime.timedelta(1)
print(str(delta).split(',')[0])
