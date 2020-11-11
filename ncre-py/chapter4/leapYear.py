# 写一个判断所输入的年份是否为闰年的函数

def judge_leap_year():
    try:
        year = input("请输入年份： ")
        year = eval(year)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print("{}是闰年。".format(year))
        else:
            print("{}不是闰年。".format(year))
    except:
        print("你特么输入了个啥？！")


if __name__ == '__main__':
    while True:
        judge_leap_year()