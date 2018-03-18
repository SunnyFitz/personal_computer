a = [1]

def sanjiao(n):
    global a
    print(a)
    if n <= 0:
        print("输入有误！！！")
    else:
        for i in range(1,n + 1):
            b = a.copy()
            if i < 2:
                b.append(1)

            else:
                b.append(1)

            print(a)


if __name__ == '__main__':
    sanjiao(int(input('请输入杨辉三角行数：')))