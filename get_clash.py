import requests
import os
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

# 发起 HTTP 请求并获取网页内容
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://wanshanziwo.eu.org'  # 替换为你要爬取的网址
response = requests.get(url,headers=headers)
html = response.text
# 使用 Beautiful Soup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')
print(html)
# 提取特定内容
# 这里只是一个示例，你可以根据需要修改提取的逻辑
# body > div.container > section:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)
# 使用 CSS 选择器查找指定元素
element = soup.select_one('html > body > div.container > section:nth-child(4) > div > table > tbody > tr:nth-child(4) > td:nth-child(2)')

# 提取元素的文本内容
if element:
    text = element.text
  
    print(text)
    # 解析 URL
    parsed_url = urlparse(text)

    # 获取参数字典
    params = parse_qs(parsed_url.query)

    # 获取 rand 参数的值
    rand_value = params.get('rand', [''])[0]
    print("随机值为:",rand_value)
    clash_url="https://wanshanziwo.eu.org/clash/proxies?c=CN,HK,SG,TW,US&type=ss,ssr,vmess,trojan,vless,wireguard&acl=true&rand="+rand_value
    airport_url="https://wanshanziwo.eu.org/airport?rand="+rand_value
    print(clash_url)
    print(airport_url)
    response_clash = requests.get(clash_url,headers=headers)
    clash = response_clash.text
    print('clash.text: '+clash[:10])
    if clash.startswith('#'):
        file_path = 'clash.txt'
        if not os.path.exists(file_path):
            with open(file_path, 'x', encoding='utf-8') as file:
                file.write(clash)
                print('文件已创建并内容已写入')
        else:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(clash)
                print('内容已写入文件')
        time.sleep(5)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
    }
    response_airport = requests.get(airport_url,headers=headers)
    airport = response_airport.text
    print('airport.text: '+airport[:10])
    if airport.startswith('#'):
        file_path = 'clash_airport.txt'
        if not os.path.exists(file_path):
            with open(file_path, 'x', encoding='utf-8') as file:
                file.write(airport)
                print('文件已创建并内容已写入')
        else:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(airport)
                print('内容已写入文件')
else:
    print('Element not found.')
