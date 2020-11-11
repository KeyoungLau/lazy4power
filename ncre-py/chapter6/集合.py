# 新建两个元组s和t
s = {1010, '1010', 78.9}
t = {1010, '1010', 12.3, 1010, 1010}

print("s-t差集运算结果：", s-t)  # 差集运算s-t
print("s&t交集运算结果：", s & t)  # 交集运算s&t
print("s^t补集运算结果：", s ^ t)  # 补集运算s^t
print("s^t并集运算结果：", s | t)  # 并集运算s|t

# 用add方法将1314整数添加到集合s中
print("未将1314添加入s集合中的情况：", s)
s.add(1314)
print("用add方法将1314元素添入到集合s中的结果：", s)

# 用remove方法移除集合s中的元素1314，若1314元素不存在，则产生KeyError异常
s.remove(1314)
print("用remove方法移除集合s中的元素1314，若1314元素不存在，则产生KeyError异常:", s)

# 用clear方法清除集合t中所有元素
print(t.clear())

# 字符串，元组，列表，集合，字典都是组合数据类型
str = '知之为知之不知为不知'
# set函数主要用于将其他组合数据类型变成集合类型
str_set = set(str)
for i in str_set:
    print(i, end="")