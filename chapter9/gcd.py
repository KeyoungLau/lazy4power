# GCD作为缩写意义有多种。它通常表示最大公约数（greatest common divisor，简写为gcd
def gcd(x,y):
    # 辗转相除法
    if x < y:
        x,y = y,x  # 交换赋值，保证x比y大
    while (x % y) != 0:
        r = x % y
        x = y
        y = r
    return y
# 请输入第一个正整数：
a = eval(input())
# 请输入第二个正整数：
b = eval(input())
gcdab = gcd(a,b)
print("{}与{}的最大公约数是{}".format(a,b,gcdab))