#题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。

n = int(input('请输入一个需要分解的正数'))
lt = []
m = n

while n > 1:
    for i in range(2, n+1):
        if n % i == 0:
            n = n // i
            lt.append(str(i))
            break
if len(lt) == 1:
    print(m, '=', '1 x', m)
else:
    s = 'x'.join(lt)
    print(m, '=', s)
