# 获取用户输入的一个数显示整数部分
a = True
while a:
    num = input("请任意输入一个数,输出quit退出程序 ")
    if num == "quit":
        break
    if isinstance(num, int):
        print(num)
    else:
        num = float(num)
        print(int(num))