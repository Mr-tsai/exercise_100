#题目：将一个数组逆序输出。

a = [9, 6, 5, 4, 1]
N = len(a)
print(a)
for i in range(int(len(a)/2)):
    a[i], a[N-i-1] = a[N-i-1], a[i]
print(a)
