total=0
result1=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if ((i!=j)and(j!=k)and(k!=i)):
                result1.append(int(str(i)+str(j)+str(k)))
                total+=1
print(total)
print(result1)

元组形式（1,2,3）
import itertools
total2=0
a=[1,2,3,4]
for i in itertools.permutations(a,3):
    print(int(i))
    total2+=1
print(total2)
