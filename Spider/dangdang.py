# Author:K
# 根据设定的关键字爬取当当网图书数据,并存储到csv文件中
import requests
from lxml import etree
from fake_useragent import UserAgent
import re
import csv


def get_page(key):
    for page in range(1, 50):
        url = f'http://search.dangdang.com/?key={key}&act=input&page_index={page}'
        headers = {
            'User-Agent': UserAgent().random
        }
        response = requests.get(url=url, headers=headers)
        parse_page(response)
        print(f'page {page} over!!!')


def parse_page(response):
    """解析网页"""
    tree = etree.HTML(response.text)
    li_list = tree.xpath('//ul[@class="bigimg"]/li')
    # print(len(li_list))  # 测试
    for li in li_list:
        data = []
        try:
            # 获取书的标题,并添加到列表中
            title = li.xpath('./p[@class="name"]/a/@title')[0].strip()
            data.append(title)
            # 获取商品链接,并添加到列表中
            commodity_url = li.xpath('./p[@class="name"]/a/@href')[0]
            data.append(commodity_url)
            # 获取价格,并添加到列表中
            price = li.xpath('./p[@class="price"]/span[1]/text()')[0]
            data.append(price)
            # 获取作者,并添加到列表中
            author = ''.join(li.xpath('./p[@class="search_book_author"]/span[1]//text()')).strip()
            data.append(author)
            # 获取出版时间,并添加到列表中
            time = li.xpath('./p[@class="search_book_author"]/span[2]/text()')[0]
            pub_time = re.sub('/', '', time).strip()
            data.append(pub_time)
            # 获取评论数,并添加到列表中
            comment_count = li.xpath('./p[@class="search_star_line"]/a/text()')[0]
            comment_count = comment_count.replace('条评论', '')  # 去掉后面的“条评论"
            data.append(comment_count)
            # 获取书本的简介,并添加到列表中.由于有些书本没有简介，所以要用try
            commodity_detail = li.xpath('./p[@class="detail"]/text()')[0]
            data.append(commodity_detail)
            # 还可以尝试获取图片
        except:
            pass
        save_data(data)


def save_data(data):
    writer.writerow(data)



fp = open('python.csv', 'w', encoding='utf-8-sig', newline='')
writer = csv.writer(fp)
header = ['标题', '链接', '价格', '作者', '出版时间', '评论数', '简介']
writer.writerow(header)
key = 'python'  # input('Please input key:')
get_page(key)
fp.close()

