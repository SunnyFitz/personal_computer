import copy
a = [1]

def sanjiao(n):
    global a
    print(a)
    if n <= 0:
        print("输入有误！！！")
    else:
        b = copy.deepcopy(a)
        for i in range(1,n):
            b.append(1)
            if i < 2:
                a = copy.deepcopy(b)
            else:
                for x in range(1,i):
                    b[x] = (a[x-1]+a[x])
            a = copy.deepcopy(b)
            print(b)


if __name__ == '__main__':
    sanjiao(int(input('请输入杨辉三角行数：')))