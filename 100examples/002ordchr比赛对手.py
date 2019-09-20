a=set(['x','y','z'])
b=set(['x','y','z'])
c=set(['x','y','z'])
c-=set(('x','z'))
a-=set('x')
for i in a:
    for j in b:
        for k in c:
            if len(set((i,j,k)))==3:
                print('a:%s,b:%s,c:%s'%(i,j,k))


a,b,c=97,98,99    #ord(a),ord(b),ord(c)
JIA=[a,b,c]
flag = 0
for x in range(97,100):
    for z in range(97,100):
        if x != a and x != c and z != c and x != z:
            flag = 1
            break
    if flag:
        break
y=sum(JIA)-x-z
YI=[x,y,z]
print('x:%s,y:%s,z:%s'%(chr(x),chr(y),chr(z)))
