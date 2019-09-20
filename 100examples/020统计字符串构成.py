string=input("输入字符串：")
alp,num,spa,oth=0,0,0,0
for i in range(len(string)):
    if string[i].isspace():
        spa+=1
    elif string[i].isdigit():
        num+=1
    elif string[i].isalpha():
        alp+=1
    else:
        oth+=1
print('space: ',spa,'','digit: ',num,'','alpha: ',alp,'','other: ',oth)

