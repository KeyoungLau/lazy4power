file_name = "龟虽寿.txt"
file_obj = open(file_name, 'r', encoding='utf-8-sig')
for line in file_obj:
    print(line, end="")  # 给end参数重新赋值，替换默认的换行符
file_obj.close()
file_name = '望江南.txt'
file_obj = open(file_name, 'w',encoding='utf-8')
file_obj.write("望江南·超然台作\n")
file_obj.write("【作者】：苏轼\n")
file_obj.write("春未老，风细柳树斜斜。\n")
file_obj.write("试上超然台上看，半壕春水一城花。\n")
file_obj.write("烟雨暗千家。\n")
file_obj.write("寒食后，酒醒却咨嗟。\n")
file_obj.write("休对故人思故国，且将新火试新茶。\n")
file_obj.write("诗酒趁年华。\n")
file_obj.close()