def create_txt(filename):
    fp = open(filename,"w+")
    ch = input('输入字符串:\n').upper()
    while ch != '#': 
        fp.write(ch)
    ##    fp.write('\n')
        fp.seek(0,0)
        print(fp.read())
        ch = input('').upper()
    fp.close()

def merge_txt():
    with open('111.txt') as fp:
        a = fp.read()
    with open('222.txt') as fp:
        b = fp.read()
    with open('333.txt','w+') as fp:
        l = list(a + b)
        l.sort()
        s = ''
        s = s.join(l)
        fp.write(s)
        fp.seek(0,0)
        print(fp.read())

create_txt('111.txt')
create_txt('222.txt')
merge_txt()

