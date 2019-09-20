I = int(input('净利润:'))
bonus = 0
thresholds = [100000,100000,200000,200000,400000]
rates = [0.1,0.075,0.05,0.03,0.015,0.01]
for i in range(5):
    if I <= thresholds[i]:
        bonus += I*rates[i]
        I = 0
        break
    else:
        bonus += thresholds[i]*rates[i]
        I -= thresholds[i]
bonus += I*rates[5]
print(bonus)


I = int(input('净利润:'))
arr = [1000000,600000,400000,200000,100000,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
bonus = 0
for i in range(6):
    if I > arr[i]:
        r += (I-arr[i])*rate[i]
        print((I-arr[i])*rate[i])
        I = arr[i]
print(r)
