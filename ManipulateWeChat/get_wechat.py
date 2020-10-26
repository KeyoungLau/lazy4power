# 通过itchat获取微信好友头像
import itchat
import csv
import os
from PIL import Image  # 3.x版本的Python应该安装pillow库
from math import sqrt


def get_head_images():
    """
    头像文件输出到当前目录的HeadImages目录下
    运行之后可能要等一会
    """
    basePath = os.path.abspath('.')
    baseFolder = basePath + r'\HeadImages'
    if not os.path.exists(baseFolder):
        os.makedirs(baseFolder)
    itchat.auto_login(hotReload=False)
    friends = itchat.get_friends(update=True)
    for friend in friends:
        img = itchat.get_head_img(userName=friend["UserName"])
        path = baseFolder + "\\" + friend['NickName'] + "(" + friend['RemarkName'] + ").jpg"
        print("处理{}中".format(path))
        try:
            with open(path, 'wb') as f:
                f.write(img)
        except Exception as e:
            print(repr(e))

def joint_head_images(path_of_head_images_folder):
    """"
    :path_of_head_images_folder:存放头像图片的文件夹路径
    """
    pathList = []
    headImgPath = path_of_head_images_folder
    for item in os.listdir(headImgPath):
        imgPath = os.path.join(headImgPath, item)
        pathList.append(imgPath)

    total = len(pathList)
    line = int(sqrt(total))
    newImage = Image.new('RGB', (128 * line, 128 * line))
    x = y = 0
    for item in pathList:
        try:
            img = Image.open(item)
            img = img.resize((128, 128), Image.ANTIALIAS)
            newImage.paste(img, (x * 128, y * 128))
            x += 1
        except IOError:
            print("第%d行,%d列文件读取失败！IOError:%s" % (y, x, item))
            x -= 1
        if x == line:
            x = 0
            y += 1
        if (x + line * y) == line * line:
            break
    newImage.save("final.jpg")


def get_wechat_friends_info(outputfilename="friends_info.csv"):
    """
    获取微信好友信息，并写入csv文件
    默认文件名为friends_info.csv
    """
    itchat.auto_login(hotReload=False)
    friends = itchat.get_friends(update=True)
    headers = list(dict(friends[1]))
    with open(outputfilename, "w", encoding="utf-8-sig", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        for friend in friends[1:]:
            values = list(dict(friend).values())
            print(values)
            writer.writerow(values)


def main():
    #get_head_images()
    #joint_head_images(r"D:\git_repo\lazy4Power\ManipulateWeChat\HeadImages\\")
    get_wechat_friends_info()


if __name__ == '__main__':
    main()