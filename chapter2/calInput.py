# 获得用户输入的合法算式，并输出结果
expression1 = input("请输入一个合法算式，如1.2+3.4 ")
expression2 = eval(expression1)
print(expression1 + "的运算结果是" + str(expression2))