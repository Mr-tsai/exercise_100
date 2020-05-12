#题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

num = int(input("请输入一个数字：\n"))
x = str(num)
flag = True

for i in range(int(len(x)/2)):
    if x[i] != x[-i - 1]:
        flag = False
        break

if flag:
    print("%d是一个回文数！" % num)
else:
    print("%d不是一个回文数！" % num)
