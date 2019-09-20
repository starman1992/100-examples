from collections import *
li=[1,2,3,4,5,6,7,8,9]
deq=deque(li,maxlen=len(li))
print(li)
cut=int(input('rotate:'))
deq.rotate(cut)
print(list(deq))

a,b = li[:(len(li)-cut)],li[(len(li)-cut):]
print(b+a)

