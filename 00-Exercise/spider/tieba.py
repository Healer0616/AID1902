import requests

url = "https://tieba.baidu.com/"
# 代理
proxies = {"HTTP": "58.56.149.198:53281"}
# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"}


requests = requests.get(url, headers=headers, proxies=proxies)

requests.encoding = "utf-8"
print(requests.text)
