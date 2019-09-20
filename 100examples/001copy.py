import copy
a = [1,2,3,4,['a','b']]     
b = a                       #赋值
c = a[:]                    #浅拷贝
d = copy.copy(a)            #浅拷贝
e = copy.deepcopy(a)        #深拷贝
a.append(5)
a[4].append('c')

print('a=',a)
print('b = a   b=',b)
print('c = a[:]  c=',c)
print('d = copy.copy(a)  d=',d)
print('e = copy.deepcopy(a)  e=',e)
