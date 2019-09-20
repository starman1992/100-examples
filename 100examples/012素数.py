I = []
for i in range(101):
    for j in range(2,round(i**0.5)+1):
        if i%j==0:
            break
    else:
        I.append(i)
print(I,len(I))

def func_get_prime(n):
  return filter(lambda x: not [x%i for i in range(2, int(x**0.5)+1) if x%i ==0], range(2,n+1))
print (list(func_get_prime(100)),len(list(func_get_prime(100))))

 
