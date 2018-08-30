# -*- coding: utf-8 -*-
# @Time    : 18-8-29 下午8:59
# @Author  : de hua
# @File    : doubanbook.py
# @Software: PyCharm
import requests
from bs4 import BeautifulSoup


def clean(data):
    data = str(data.text).replace(' ', '').strip()
    data = data.replace('\n', '')
    return data


def get_data(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    name_list = soup.select('h2 > a')
    bookinfo_list = soup.select('div.pub')
    ratingnum_list = soup.select('div.star.clearfix > span.rating_nums')
    view_list = soup.select('div.info > p')
    url_list = soup.select('h2 > a')
    pl_list = soup.select('span.pl')
    for name, bookinfo, ratingnum, pl, url, view in zip(name_list, bookinfo_list, ratingnum_list, pl_list, url_list,
                                                        view_list):
        book = {
            'name': clean(name),
            'bookinfo': clean(bookinfo),
            'ratingnum': clean(ratingnum),
            'pl': clean(pl),
            'url': url.get('href'),
            'view': clean(view)
        }
        print(book)


def get_page():
    i = 0
    while i < 1000:
        url = 'https://book.douban.com/tag/2018%E4%B9%A6%E5%8D%95?start=' + str(i) + '&type=T'
        get_data(url)
        i += 20


if __name__ == '__main__':
    get_page()
