from random import *
r = random()  # random函数生成一个[0.0, 1.0)之间的随机小数
print(r)
# seed()函数对后续产生的伪随机数设置种子a
# 种子相同，生成的随机数也相同
# randint()用于生成[a,b]之间的随机整数
i = randint(0, 9)
print(i)
# getrandbits()函数用于生成一个k比特长度的随机整数
# sample()函数用于从pop中随机选取k个元素，以列表类型返回，注意，pop中所含的元素要不少于k个,population
ls = [1, 2, 3, 4, 5, 6, 7, 8]
s = sample(ls,3)
print(s)
print(ls)