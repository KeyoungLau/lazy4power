# 爬取糗事百科的笑话
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6776.400 QQBrowser/10.3.2601.400'
}


def get_pages(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'lxml')
    pages=[]
    for page in soup.select('span[class="page-numbers"]'):
        p = int(page.get_text().strip())
        pages.append(p)
    return max(pages)

def generate_urls(x):
    urls = []
    for i in range(1, x+1):
        urls.append('https://www.qiushibaike.com/text/page/{}/'.format(i))
    return urls



def parser_one_page(url):
    res =requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text,'lxml')
    for content in soup.select('div[class="content"] > span'):
        print('\n'+content.get_text().strip())
        print('-'*70)


def main():
    url = 'https://www.qiushibaike.com/text/'
    number = get_pages(url)
    uu = generate_urls(number)
    for u in uu:
        parser_one_page(u)


if __name__ == '__main__':
    main()