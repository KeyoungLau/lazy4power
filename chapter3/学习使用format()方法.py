str = "{2}叫小兵，我在{0}出生，我喜欢{1}".format("1997-05-01","English","我")
print(str)
# <格式控制标记>包括：<填充><对齐><宽度>,<.精度><类型>六个字段，可以组合使用。
str1 = "PYTHON"
str2 = "PHP"
num = 18843798579832
fnum = -145.67893234
print("{0:=^40}{1:+^50}{2:,}".format(str1, str2, num))  # 参数控制标记中不能写成40^
print("{0:+.2f}".format(fnum))
print("{:.2f}".format(3.14))
N = eval(input())   # N取值范围是0—100，整数
print("{:>3}%@{}".format(N,"="*(N//5)))