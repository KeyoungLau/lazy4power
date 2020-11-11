# 输入整数N，计算并输入1到N相加的和
n = input("整数N： ")
n = int(n) + 1
sum = 0
for i in range(n):
    sum = sum + i
n = n - 1
print("1到" + str(n) + "求和结果：{}".format(sum))

