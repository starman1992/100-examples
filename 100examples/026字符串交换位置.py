li=[3,2,5,7,8,1,5]
li[-1],li[li.index(min(li))]=li[li.index(min(li))],li[-1]
li[li.index(max(li))],li[0]=li[0],li[li.index(max(li))]
print(li)
