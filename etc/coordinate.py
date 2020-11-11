# 监视剪切板，将剪切板中特定格式的数据读取出来，再进行格式化输出
# 识别转化特定格式的经纬度地址
# 这个文件存在的意义在于：我们可以操纵系统的剪切板
# 运行这个程序，然后复制示例数据，看看有什么效果
# 示例数据：贵州省贵阳市云岩区书香门第B栋3单元:106.725241,26.594446
import re
import pyperclip
import time

last_string = pyperclip.paste()
print(last_string)
while True:
    time.sleep(3)
    raw_address = pyperclip.paste()
    if raw_address == last_string or raw_address == '':
        pass
    else:
        if re.match(".*:[0-9.].*,[0-9.].*", raw_address):
            slice1 = re.findall("(.*):", raw_address)
            slice2 = re.findall(":([0-9.].*),", raw_address)
            slice3 = re.findall(",([0-9.].*)", raw_address)
            print(slice1[0])
            print(f"北_{slice3[0]}")
            print(f"东_{slice2[0]}")
            print("-" * 20)
            last_string = raw_address
            #print("raw_add",raw_address)
            #print("last_string", last_string)
        else:
            pass