import requests

import re

content = requests.get("https://book.douban.com/").text
pattern = re.compile(
    '<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
results = re.findall(pattern, content)
# print(results)
for res in results:
    url, name, author, date = res
    author = re.sub("\s", "", author)
    date = re.sub("\s", "", date)
    print(url, name, author, date)
