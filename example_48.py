#题目：数字比较。

print('比较两个数字的大小：')
x = int(input("请输入第一个数字："))
y = int(input("请输入第一个数字："))
if x > y:
    print('%d 大于 %d' % (x, y))
elif x == y:
    print('%d 等于 %d' % (x, y))
elif x < y:
    print('%d 小于 %d' % (x, y))
else:
    print('未知')
