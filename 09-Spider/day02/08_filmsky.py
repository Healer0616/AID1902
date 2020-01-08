from urllib import request
import re
import time
import random
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class FilmSkySpider(object):
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    # 获取响应内容(两级页面)
    def get_page(self, url):
        req = request.Request(
            url,
            headers=self.headers
        )
        res = request.urlopen(req)
        # decode()第二个参数，ignore 忽略掉解码异常
        html = res.read().decode('gb18030', 'ignore')

        return html

    # 解析一级页面
    def parse_one_page(self, html):
        pattern = re.compile('<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">(.*?)</a>.*?</table>',
                             re.S)
        film_list = pattern.findall(html)
        # print(film_list)
        for film in film_list:
            # 电影名称
            name = film[1].strip()
            # 电影链接
            link = 'https://www.dytt8.net' + film[0].strip()
            # 向link发请求，获取下载链接（二级页面）
            download_link = self.get_two_page(link)

            print([name,link])

    # 解析二级页面
    def get_two_page(self, link):
        # 发请求
        html = self.get_page(link)
        # 解析
        pattern = re.compile('<td style="WORD-WRAP.*?>.*?>(.*?)</a>', re.S)

        return pattern.findall(html)[0]


if __name__ == "__main__":
    url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_1.html'
    spider = FilmSkySpider()
    html = spider.get_page(url)
    spider.parse_one_page(html)
