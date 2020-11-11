def isNum(x):
    if type(x) == type(5):
        return True
    if type(x) == type(1.1):
        return True
    if type(x) == type(2.4+5.6j):
        return True
    else:
        return False

if __name__ == '__main__':
    print(isNum(x='演讲'))