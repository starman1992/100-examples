a,b=2,1
c=a/b
for i in range(19):
    a,b=a+b,a
    c+=a/b
print(a,b,c)
