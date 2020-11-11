
from pydocx import PyDocX
import re
path = r'C:\Users\Keyou\Desktop\新建 Microsoft Word 文档 (2).docx'

# Pass in a path
html = PyDocX.to_html(path)
#print(type(html))
res = re.findall("<p>.*?</p>", html)
print(res)
for i in range(len(res)):
    res[i] = res[i].replace("<p>", "")
    res[i] = res[i].replace("</p>", "")

fill_in_blank_lst = []
for i in res:
    #print(len(i))
    tem_lst = []
    if "//" in i:
        tags = re.findall("//.*", i)[0]
        #print(len(tags))
        new_index = len(i) - len(tags)

        # 把tags标识符//用replace方法给替代掉
        tags = tags.replace("//", "")

        ques = i[0: new_index - 1]  # 由于加了空格，要把空格截断不要，就还要把索引减1
        tem_lst.append(ques)
        tem_lst.append(ques)
        tem_lst.append(tags)

    else:
        # 没有tags的情况
        ques = i
        tags = ""  # 写一个空tags
        #print(ques)
        tem_lst.append(ques)
        tem_lst.append(ques)
        tem_lst.append(tags)
    fill_in_blank_lst.append(tem_lst)
print(fill_in_blank_lst)


# 开始处理strong标签，可以处理成想要的形式
for item in fill_in_blank_lst:
    if ("<strong>" or "</strong>") in item[0]:  # 还要考虑忘记标记粗体的情况
        key_points = re.findall("<strong>(.*)</strong>", item[0])
        #print(key_points)
        item[0] = item[0].replace("<strong>", "")
        item[0] = item[0].replace("</strong>", "")

        item[1] = item[1].replace("<strong>", " r/ ")
        item[1] = item[1].replace("</strong>", " / ")
        #print(item)



        '''for key_point in key_points:
            key_point = key_point.replace("<strong>", "")
            key_point = key_point.replace("</strong>", "")  # 替换strong标签
            item[0] = item[0].replace("<strong>", "")
            item[0] = item[0].replace("</strong>", "")
            answer = item[0].replace(key_point, "r/" + key_point + "/")
            print(answer)'''
    else:
        pass  # 等会

#print(fill_in_blank_lst)

# 处理成KeyoungBasic-Blank模板需要的形式
from datetime import datetime
nowTime = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
import csv

if fill_in_blank_lst:
    out_file = "填空" + nowTime + ".csv"
    with open(fr"C:\Users\Keyou\Desktop\{out_file}", "a+", encoding="utf-8-sig", newline='') as f_obj:
        writer = csv.writer(f_obj)
        for i in range(len(fill_in_blank_lst)):
            print("写入内容", fill_in_blank_lst[i])
            writer.writerow(fill_in_blank_lst[i])
        print(f"CSV文件<{out_file}>填空题写入完毕。")
        print("=====" * 20)
else:
    # else代表new_single_lst是空的，没有数据要写入
    print("无填空题数据要写入。")
    print("=====" * 20)