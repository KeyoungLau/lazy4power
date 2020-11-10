try:
    n=input("请输入一个数字:")
    assert n.isdigit(),"只能输入数字"
    print("你输入的是：",n)
except Exception as ex:
    print("发现错误:",ex)


