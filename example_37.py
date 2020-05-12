#题目：对10个数进行排序。

N = 10
print('请输入10个数字：\n')
l = []
for i in range(N):
    l.append(int(input('请输入一个数字：\n')))
print()
for i in range(N):
    print(l[i])
print()

for i in range(N-1):
    min_num = i
    for j in range(i+1, N):
        if l[min_num] > l[j]:
            min_num = j
    l[i], l[min_num] = l[min_num], l[i]
print('排列之后：')
for i in range(N):
    print(l[i])
