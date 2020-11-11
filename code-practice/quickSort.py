def quicksort(array):
    # 快速排序算法
    less = []
    greater = []
    if len(array) <= 1:
        return array
    pivot = array.pop()
    for x in array:
        if x <= pivot:
            less.append(x)
        else:
            greater.append(x)
    return quicksort(less) + [pivot] + quicksort(greater)  # 迭代思想很重要，可以少些很多代码


def main():
    print(quicksort([5, 48, 78, 69, 4, 1]))


if __name__ == '__main__':
    # min()
    # 为什么main函数会报错
    print(quicksort([5, 48, 78, 69, 4, 1]))
