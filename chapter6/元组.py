s = list()
for i in range(11):
    s.append(i)
# 用tuple()函数把列表s转换为元组
s = tuple(s)
print("原元组为：", s)
# 对列表s进行切片，步长为2
print("从第四个开始对元组进行切片，步长为2： ",s[3::2])