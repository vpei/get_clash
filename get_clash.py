import requests
import os
from bs4 import BeautifulSoup

# 发起 HTTP 请求并获取网页内容
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
url = 'https://wanshanziwo.eu.org/clash'  # 替换为你要爬取的网址
response = requests.get(url,headers=headers)
html = response.text
# 使用 Beautiful Soup 解析 HTML
soup = BeautifulSoup(html, 'html.parser')
print(html)
# 提取特定内容
# 这里只是一个示例，你可以根据需要修改提取的逻辑
# body > div.container > section:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)
# 使用 CSS 选择器查找指定元素
element = soup.select_one('html > body > div.container > section:nth-child(2) > div > div > table > tbody > tr:nth-child(1) > td:nth-child(2)')

# 提取元素的文本内容
if element:
    text = element.text
    response_clash = requests.get(text)
    clash = response_clash.text
    print(clash)
    file_path = 'clash.txt'
    if not os.path.exists(file_path):
        with open(file_path, 'x', encoding='utf-8') as file:
            file.write(clash)
            print('文件已创建并内容已写入')
    else:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(clash)
            print('内容已写入文件')
else:
    print('Element not found.')
