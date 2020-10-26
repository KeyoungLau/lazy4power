# author:keyoung.lau
# email:keyoung.lau@outlook.com
# date:2020-10-26
# python-version:3.x
"""
以学位证的OCR识别和重命名来演示百度云的OCR用法
这是去年给云南大学校档案馆做的一个小工具
OCR比较有意思，对提高工作效率很有帮助，就记录下来了
云大每年有近万人毕业生，学校档案馆要对这些毕业生的毕业证和学位证信息重命名
以人工来做耗时又费力，极度无聊
文件重命名的依据是根据图片中学生的姓名，专业和学院等信息
传统的批量重命名工具不能处理这种情况
所以可以通过OCR识别把这些信息给提取出来
百度云OCR对中文的识别效果比较好
pip install baidu-aip
需要安装baidu-aip这个包，如果没安装就要自行安装
百度云OCR申请，https://ai.baidu.com/tech/ocr
高精度每天可以调用500次，标准版每天可以调用50000次
"""

from aip import AipOcr
import re
import os


def construct_path():
    """
    路径构造函数,构造存放待处理图片的目录的绝对路径
    """
    path = os.getcwd()  # 获取当前工作目录
    path += r"\sampleFiles\专硕"
    return path


def get_file_content(filePath):
    """
    传入一个文件路径，以字节流形式读取文件内容
    在这里主要用于读取图片
    """
    with open(filePath, 'rb') as fp:
        return fp.read()


def identify_image(file):
    """
    调用百度云OCR进行图片文字识别
    调用通用文字识别, 图片参数为本地图片
    """
    APP_ID = '17114470'
    API_KEY = 'giNbD8jEWclDspoPvHI3sF3j'
    SECRET_KEY = 'Lk2CHrdfHp2Q2VHSOWdSAblOzOuGG7wG'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    options = {}
    results = client.basicAccurate(get_file_content(file), options=options)
    if 'words_result' in results.keys():  # 如果有'words_result'，表示有识别结果
        string = '\n'.join([w['words'] for w in results['words_result']])
        # name和major都是一个列表
        name = re.findall('研究生(\w{2,10})性别', string)  # 人名最少两个字，最多10个字
        major = re.findall('在\n(\w{1,})\n专业|在(\w{1,})\n', string)
        return name, major


def main():
    path = construct_path()
    for item in os.listdir(path):  # 遍历该路径下所有文件
        abs_filePath = path + "\\" + item  # 构造文件的绝对路径
        print(abs_filePath)
        # 调用通用文字识别, 图片参数为本地图片
        name, major = identify_image(abs_filePath)
        print(name)
        print(major)
        print("-" * 30)
        # 重命名
        if name:
            # 对major进行一下判断
            if major[0][0]:
                os.rename(abs_filePath, path + r'\历史与档案学院2019届{}{}硕士研究生毕业证书.jpg'.format(major[0][0], name[0]))
            if major[0][0] == '':
                os.rename(abs_filePath, path + r'历史与档案学院2019届{}{}硕士研究生毕业证书.jpg'.format(major[0][0], name[0]))


if __name__ == '__main__':
    main()