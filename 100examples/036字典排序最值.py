person = {"li":18,"wang":50,"zhang":20,"sun":22}
b=max(zip(person.values(),person.keys()))   #最大值对应键
c=zip(person.values(),person.keys())        #排序
print(b[1])
print(sorted(c))
