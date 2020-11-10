import openpyxl
import os

input_file_path = r"C:\Users\Keyou\Desktop\ncreMySQL.xlsx"  # 单选路径

#input_file_path = r"C:\Users\Keyou\Desktop\anki模板\anki测试文件\多选题测试\多选题测试.xlsx"  # 多选路径

#input_file_path = r"C:\Users\Keyou\Desktop\新建 Microsoft Excel 工作表 (2).xlsx"  # 判断路径
wb = openpyxl.load_workbook(input_file_path)
work_sheet1 = wb.worksheets[0]  # 激活工作表


def data_pre_processing(worksheet):
    """
    传入一个工作表,返回一个处理好的清洗好二维数据表
    :param worksheet:
    :return:
    """
    #读取原始数据到一个二维列表
    data = list(worksheet.rows)

    # 对数据进行一个预处理
    oranges = []
    for rows in range(len(data)):
        tem_lst = [i.value for i in data[rows]]  # 列表解析，cool，优雅
        tem_lst =list(filter(None, tem_lst))  #   # 剔除掉tem_lst中的None值
        tem_lst = [str(i) for i in tem_lst]  # 把tem_lst转化为纯数字列表,避免数字没有下标的问题
        oranges.append(tem_lst)  #  把tem_lst加入到oranges列表中
    #print(oranges)
    return oranges
    #从头抽出第一条数据，就命名为apple吧
    #apples = [i.value for i in data[0]]  # 列表解析，cool，优雅

    # 剔除掉apple中的None值
    #apples = list(filter(None, apples))

    # 把apple转化为纯数字列表,避免数字没有下标的问题
    #apples.append("我是一个粉刷匠。")
    #apples = [str(i) for i in apples]
    #print(apples)


single_lst = []
multi_lst = []
yes_or_no_lst = []
fill_in__blank_lst = []
unrecognized_lst = []  # 五个菜篮子，第五个菜篮子unrecognized_lst用于存放不能识别的数据

def judge_types(apples):
    """
    传入列表，首先判断是否输入extra类型，再判断属于哪种题型（单选，多选，判断，填空），至于如何返回，还得好好考虑考虑
    :param list:
    :return:
    """
    # 调用四个全局变量储存结果
    global single_lst, multi_lst, yes_or_no_lst, fill_in__blank_lst, unrecognized_lst
    # 先判断apples是否有tags,双斜线为tags标识符
    tags = ""  # 建立一个空tags
    if "//" in apples[-1]:
        print(apples, "有tags。")
        # 把tags弹出来
        tags = apples.pop()
        # 把tags的双斜线替换掉
        tags = tags.replace("//", "")
    else:
        # 没有tags就不抽，但也要打印一条说明
        print(apples, "没有tags。")



    # 先判断apples是否属于extra类型，其实有两种判断方法
    # 先设定一个extra变量，extra变量初始值为四个空格
    extra = "    "
    if (apples[-1][-1] == "。") or (apples[-1][-1] == "."):
        print(apples, "是extra类型。")
        # 把extra给弹出来，储存在extra变量里面,等于给extra变量重新赋值，extra不是四个空格了
        extra = apples.pop()
        #print(extra)
    else:
        # 不管是不是extra类型，都要打印一条语句说明情况
        print(apples, "不是extra类型。")


    # 设定规则：填空题为了不与单选题混淆，填空题需要在答案后一列添加"*"标识符
    if "*" in apples[-1]:
        # 既然断定了是填空题类型，标识符*先别删
        #del apples[-1]
        print(apples, "是填空题类型。")
        fill_in__blank_lst.append(apples.copy())  # 添加到fill_in__blank_lst中
        apples.clear()
        print("=====" * 20)


    # 为判断题设定规则：判断题的标识符为：对，错，t，f，T，F
    check_yes_or_no_answers = ["t", "f", "T", "F", "对", "错", "1", "0"]  # 这里的0在excel中输入的时候必须是强制文本格式['0]
    if apples[-1] in check_yes_or_no_answers:
        # 判断标识符是否在检查字典键里面
        #print(apples, "是判断题类型。")
        #还要把判断题类型转化为单选题类型，建立一个正确类型的列表
        check_yes_or_no_answers_true = ["t", "T", "对", "1"]
        if apples[-1] in check_yes_or_no_answers_true:
            apples[-1] = "对"  # 把标识符统一换成"对"
            apples.append("错")  # 再加一个对立的错
        else:
            apples[-1] = "错"  # 把标识符统一换成"错"
            apples.append("对")  # 再加一个对立的"对"
        # 把extra内容加上去
        apples.append(extra)
        # 把tags加上去
        apples.append(tags)
        print(apples, "是判断题类型。")
        # 建立apples拷贝到yes_or_no_lst
        yes_or_no_lst.append(apples.copy())
        apples.clear()
        print("=====" * 20)


    # 创建一个检查选择题类型的列表
    check_multi_answers = ["A", "B", "C", "D", "E", "F", "G"]
    # 创建一个couter计数器来区分单选题和多选题
    counter = 0

    # apple不为空，就代表不是上面两种类型
    if apples:
        # 选项全部转写为大写
        apples[-1] = apples[-1].upper()
        # 遍历字符串,计算出现的次数
        for char in apples[-1]:
            if char in check_multi_answers:
                counter += 1
        #print(counter)



    # counter=1就说明是单选题类型
    if counter == 1:
        print(apples, "是单选题类型。")
        # 由于模板的原因，要做一下位置变换，把正确答案取出来，放在第二列，也就是问题的后面那一列,建立一个字典来处理这个问题
        check_single_answers= {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8}
        right_answer_index = check_single_answers.get(apples[-1], 1)  # 如果没查到正确答案的索引，就返回1把A当作正确选项

        # 分情况处理答案是a和不是a的情况
        if right_answer_index == 1:  # 处理一下答案是a的情况
            # 把extra加上去
            apples.append(extra)
            # 把tags加上去
            apples.append(tags)
            print(apples, "处理过后")
            single_lst.append(apples.copy())
            apples.clear()
            print("====="*20)
        else:
            # 再答案不是A的情况下，要把正确答案先拿出来,再重新插入到列表中,还要把apples[-1]改为A，因为正确答案已经变成了A,
            # 用pop把正确答案拿出来
            right_answer = apples.pop(right_answer_index)

            # 由于模板的原因，需要用insert把right_answer插入到问候后面那一列,还需要把答案全部改为A,不然答案和选项对不上
            apples.insert(1, right_answer)
            apples[-1] = "A"

            #print(right_answer)

            #  Answer本来要删除的，但为了和多选题模板保持一致，这里就不删除了，采用在anki单选题模板中第三位添加Answer字段来解决

            # 把extra内容加到末行
            apples.append(extra)
            # 把tags加上去
            apples.append(tags)
            print(apples, "处理过后")
            single_lst.append(apples.copy())
            apples.clear()
            print("=====" * 20)


    #  counter不等于1就说明是双选题类型
    elif counter >= 2:
        # 由于多选题模板原因，答案不能像单选题这样删除，要保留
        print(apples, "是多选题类型。")
        # 把extra内容加上去
        apples.append(extra)
        # 把tags加上去
        apples.append(tags)
        print(apples)
        # 把apples加入到列表 multi_lst中
        multi_lst.append(apples.copy())
        apples.clear()
        print("=====" * 20)
        # 把多选题加入到multi_lst中

    # 流到这里的数据都是前面不能识别的数据，丢到unrecognized_lst中,设置一个计数器来提示
    #counter = 0
    if apples:  # 如果apples还存在
        #counter += 1
        unrecognized_lst.append(apples)
        print(f"有{apples}数据未被识别，写入到unrecognized_lst中。")
        print("=====" * 20)

    #return single_lst, multi_lst, fill_in__blank_lst, yes_or_no_lst










def single_choice(single_lst):
    """
    传入一个单选题列表进行处理，单选题模板用的是易小猫的制作的模板
    :param single_lst: a list can be handle
    :return:
    """
    import csv
    global time_stamp

    print(f"开始处理单选题数据，单选题数据有{len(single_lst)}条。")

    #括号替换
    brackets_lst = ["()", "（）", "[]", "【】", "{}", "<>"]
    for item in single_lst:
        replace_item = "{{c1::" + item[1] + "}}"  # 模板原因，单选题的replace_item是一个变化的，需要变一下
        #print(replace_item)
        for bracket in brackets_lst:
            if bracket in item[0]:
                item[0] = item[0].replace(bracket, replace_item)  # 进行一个替换操作
                #break
                #print(item[0])


        # 再考虑问题没有括号的情况,在末尾加上replace_item
        if replace_item not in item[0]:
            item[0] = item[0] + replace_item

    #print(single_lst)

    # 开始加<br>符号
    new_single_lst = []
    for item in single_lst:
        #print(item)
        new_list = []
        tem_list = item[1: -3]
        #print(tem_list)
        tem_str = "<br>".join(tem_list)
        new_list.append(item[0])
        new_list.append(tem_str)
        new_list.append(item[-3])
        new_list.append(item[-2])
        new_list.append(item[-1])  # 用excel打开可能出错，但csv直接导入就可以了，别管excel
        #print(new_list)
        new_single_lst.append(new_list)  # new_single_lst就是处理好的单选题数据

    # 开始准备写入文件
    if new_single_lst:
        # new_single_lst不为空，就代表有单选题数据
        out_file = "单选题" + time_stamp + ".csv"
        with open(fr"C:\Users\Keyou\Desktop\{out_file}", "a+", encoding="utf-8-sig", newline='') as f_obj:
            writer = csv.writer(f_obj)
            for i in range(len(new_single_lst)):
                print("写入内容", new_single_lst[i])
                writer.writerow(new_single_lst[i])
            print(f"CSV文件<{out_file}>单选题写入完毕。")
            print("=====" * 20)
    else:
        # else代表new_single_lst是空的，没有数据要写入
        print("无单选题数据要写入。")
        print("=====" * 20)



def multi_choice(multi_lst):
    """
    一个处理多选题列表的函数,主要适用于GoldException的多选题模板
    :param multi_lst:
    :return:
    """
    import os
    import csv
    global time_stamp


    print(f"开始处理多选题数据，多选题数据有{len(multi_lst)}条。")
    # 括号替换
    brackets_lst =["()", "（）", "[]", "【】", "{}", "<>"]
    replace_item = "{{c1::（）}}"
    for item in multi_lst:
        for bracket in brackets_lst:
            if bracket in item[0]:
                item[0] = item[0].replace(bracket, replace_item)  # 进行一个替换操作
                # 要不要加个break或者continue呢？

        if replace_item not in item[0]:
            item[0] = item[0] + replace_item


    # 再考虑没有括号的情况,在末尾加上replace_item
    #for item in multi_lst:
        #if replace_item not in item[0]:
            #item[0] = item[0] + replace_item

    #print(multi_lst)

    #  加标识符号A.,B.,C.,一番魔法变换
    index_identifier = ["A.", "B.", "C.", "D.", "E.", "F.", "H."]
    new_multi_lst = []
    for item in multi_lst:
        tem_list = item[1: -2]
        #print(tem_list)
        #print(item)
        zipped = zip(index_identifier, tem_list)
        new_list = []
        for i in zipped:
            new_list.append(i[0] + i[1])  # 重新组合
        tem_str = "<br>".join(new_list)
        new_list.clear()
        #print(tem_str)
        new_list.append(tem_str)
        new_list.insert(0, item[0])
        new_list.append(item[-2])
        new_list.append(item[-1])
        new_multi_lst.append(new_list)  # new_multi_lst就是处理好的数据
    #print(new_multi_lst)

    # 如果new_multi_lst不为空，代表有多选题数据，就要开始写入
    if new_multi_lst:
        out_file = "多选题" + time_stamp + ".csv"
        with open(fr"C:\Users\Keyou\Desktop\{out_file}" , "a+", encoding="utf-8-sig", newline='') as f_obj:
            writer = csv.writer(f_obj)
            for i in range(len(new_multi_lst)):
                print("写入内容", new_multi_lst[i])
                writer.writerow(new_multi_lst[i])
            print(f"CSV文件<{out_file}>多选题写入完毕。")
            print("=====" * 20)
    else:
        # else代表new_multi_lst是空的，没有数据要写入
        print("无多选题数据要写入。")
        print("=====" * 20)






def yes_or_no_quest(yes_or_no_lst):
    """
    一个处理判断题的函数，判断题也是一种简单的选择题,所以判断题的anki模板还是基于易小猫的单选题模板
    判断题传入的正确答案可能有：对，错，t，f，T，F，1，0等值
    :param list:
    :return:
    """
    #print("hello")
    import csv
    global time_stamp

    print(f"开始处理判断题数据，判断题数据有{len(yes_or_no_lst)}条。")

    # 括号替换
    brackets_lst = ["()", "（）", "[]", "【】", "{}", "<>"]
    for item in yes_or_no_lst:
        replace_item = "{{c1::" + item[1] + "}}"  # 模板原因，单选题的replace_item是一个变化的，需要变一下
        # print(replace_item)
        for bracket in brackets_lst:
            if bracket in item[0]:
                item[0] = item[0].replace(bracket, replace_item)  # 进行一个替换操作
                # break
                # print(item[0])

        # 再考虑问题没有括号的情况,在末尾加上replace_item
        if replace_item not in item[0]:
            item[0] = item[0] + replace_item
    #print(yes_or_no_lst)

    # 开始加选项A
    for item in yes_or_no_lst:
        item.insert(-2, "A")
    #print(yes_or_no_lst)

    # 开始加<br>符号
    new_yes_or_no_lst = []
    for item in yes_or_no_lst:
        # print(item)
        new_list = []
        tem_list = item[1: -3]
        # print(tem_list)
        tem_str = "<br>".join(tem_list)
        new_list.append(item[0])
        new_list.append(tem_str)
        new_list.append(item[-3])
        new_list.append(item[-2])
        new_list.append(item[-1])
        #print(new_list)
        new_yes_or_no_lst.append(new_list)  # new_yes_or_no_lst就是处理好的单选题数据

    # 开始准备写入文件
    if new_yes_or_no_lst:
        # new_yes_or_no_lst不为空，就代表有判断题数据
        out_file = "判断题" + time_stamp + ".csv"
        with open(fr"C:\Users\Keyou\Desktop\{out_file}", "a+", encoding="utf-8-sig", newline='') as f_obj:
            writer = csv.writer(f_obj)
            for i in range(len(new_yes_or_no_lst)):
                print("写入内容", new_yes_or_no_lst[i])
                writer.writerow(new_yes_or_no_lst[i])
            print(f"CSV文件<{out_file}>判断题写入完毕。")
            print("=====" * 20)
    else:
        # else代表new_single_lst是空的，没有数据要写入
        print("无判断题数据要写入。")
        print("=====" * 20)




def generate_time_stamp():
    """
    生成一个统一的时间戳，用于文件命名
    :return:
    """
    from datetime import datetime
    nowTime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    return nowTime













if __name__ == '__main__':
    print("=====" * 20)
    time_stamp = generate_time_stamp()
    data = data_pre_processing(work_sheet1)
    for item in data:
        #print(item)
        judge_types(item)  # 等于这是一个分拣的过程
    multi_choice(multi_lst)  # 先处理多选
    single_choice(single_lst)
    yes_or_no_quest(yes_or_no_lst)
    #print(single_lst)
    #print(multi_lst)
    #print(fill_in__blank_lst)
    #print("yes_or_no_lst:", yes_or_no_lst)
    print("unrecognized_lst:", unrecognized_lst)

    