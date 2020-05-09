#题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

#落地次数
tim = 10
#弹起高度
height = []
#弹起总路程
total = []
#起始高度
high = 100

for i in range(1, tim+1):
    if i == 1:
        total.append(high)
    else:
        total.append(2*high)
    high = high / 2
    height.append(high)
print('总路程：{0}'.format(sum(total)))
print('第10次反弹的高度：{0}'.format(height[-1]))
