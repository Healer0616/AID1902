import requests

url = 'http://b.hiphotos.baidu.com/zhidao/pic/item/9a504fc2d5628535e4b1633a92ef76c6a7ef6353.jpg'
headers = {
    'User-Agent':'Mozilla/5.0'
}

html = requests.get(url,headers=headers).content
with open('pokemon.jpg','wb') as f:
    f.write(html)