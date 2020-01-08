import requests
from lxml import etree

url = 'http://www.renren.com/971300734/profile'
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "anonymid=jxcu7die6o354s; depovince=ZJ; _r01_=1; JSESSIONID=abcNQgBBB9SBG7c0zzsUw; ick_login=cebd9944-c4aa-4544-97cd-9753cf512b59; loginfrom=null; wp_fold=0; ick=227e38d3-2d9a-4e72-ad46-7dc67acc993d; t=8fdb22f3a8f74fa4780038c43ffb86a34; societyguester=8fdb22f3a8f74fa4780038c43ffb86a34; id=971300734; xnsid=6d89ff07; jebecookies=edba369f-03f7-40f4-b807-0516fe7a2b06|||||; ver=7.0",
    "Host": "www.renren.com",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

html = requests.get(url, headers=headers).text
parse_html = etree.HTML(html)
result = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')[0].strip()
print(result)
