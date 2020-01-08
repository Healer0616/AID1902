from urllib import request
import csv
import time
import re
import random
import pymongo


class MaoyanSpider(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4?offset={}'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        # 添加计数变量
        self.page = 1
        # 创建3个对象
        self.conn = pymongo.MongoClient('localhost',27017)
        self.db = self.conn['maoyandb']
        self.myset = self.db['filmset']

    def get_page(self, url):
        req = request.Request(
            url,
            headers=self.headers
        )
        res = request.urlopen(req)
        html = res.read().decode("utf-8")
        # 直接调用解析函数
        self.parse_page(html)

    def parse_page(self, html):
        pattern = re.compile(
            '<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>', re.S)
        film_list = pattern.findall(html)
        # film_list:[('"$1":"$2"别姬','张国荣','1993')]
        self.write_mongo(film_list)

    def write_mongo(self, film_list):
        for film in film_list:
            film_dict = {
                '名称':film[0].strip(),
                '主演':film[1].strip(),
                '时间':film[2].strip()
            }
            # 插入数据库
            self.myset.insert_one(film_dict)

    # def write_csv(self, film_list):
    #     with open("maoyanfilm.csv", "a") as f:
    #         # 初始化写入对象
    #         writer = csv.writer(f)
    #         for film in film_list:
    #             # ('"$1":"$2"别姬','\n张国荣 ','1993')
    #             L = [
    #                 film[0].strip(),
    #                 film[1].strip(),
    #                 film[2].strip()
    #             ]
    #             writer.writerow(L)

    def main(self):
        for offset in range(0, 91, 10):
            url = self.url.format(str(offset))
            self.get_page(url)
            print('第{}页完成'.format(self.page))
            self.page += 1
            time.sleep(random.randint(1, 3))


if __name__ == "__main__":
    spider = MaoyanSpider()
    spider.main()
