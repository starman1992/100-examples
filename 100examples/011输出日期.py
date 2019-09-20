import datetime
print(datetime.date.today())
print(datetime.date(2333,2,3))
print(datetime.date.today().strftime('%d/%m/%Y'))
day=datetime.date(1111,2,3)
day+=datetime.timedelta(1)
print(day)
day=day.replace(year=day.year+22)
print(day)
