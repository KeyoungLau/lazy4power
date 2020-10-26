# 删除广告词的反向操作，添加广告词
import os
import os.path


def remove_ad_text(path:str, ad_text="[www.abc.com]"):
    """
    用来删除特点广告文本的函数。
    该函数会搜索检查指定根目录下的所有文件及子目录，如果子目录下依然存在子目录，则会一直查找下去，直到没有子目录为止。然后将目录名与文件名中含有的广告词删除。
    :param path:指定要检查的目录
    :param ad_text:指定要删除的广告词
    :return:
    """

    # 如果path表示的不是一个目录，则直接返回。
    if not os.path.isdir(path):
        return

    # 如果传递的path末尾没有路径分隔符，我们就加入路径分隔符
    if not path.endswith(os.path.sep):
        path += os.path.sep

    # 获取目录下所有的子目录以及文件名.（返回列表类型）
    names = os.listdir(path)
    #print(names)
    # 依次遍历每一个子目录或文件名。（对子目录和文件的处理方式是不同的）
    for name in names:
        # 拼接成完整路径
        sub_path = os.path.join(path, name)
        # 判断该路径表示的是否为目录
        if os.path.isdir(sub_path):
            # 如果是目录，则要进行递归的判断查找（下钻）
            # 递归是函数调用自身的过程
            remove_ad_text(sub_path)
        # 将当前文件（目录）进行重命名，去掉广告词
        name = ad_text + name
        # 组合新的路径
        new_path = os.path.join(path, name)
        # 对文件（目录）名进行重命名
        os.rename(sub_path, new_path)



def main():
    path = r'C:\Users\Keyou\PycharmProjects\Automation\FileRename\下载的文件'
    remove_ad_text(path)


if __name__ == '__main__':
    main()