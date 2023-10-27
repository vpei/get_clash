import requests
import os
import time
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

def get_html_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    return response.text

def write_to_file(file_path, content):
    mode = 'x' if not os.path.exists(file_path) else 'w'
    with open(file_path, mode, encoding='utf-8') as file:
        file.write(content)
        print('内容已写入文件')

def scrape_website():
    url = 'https://wanshanziwo.eu.org'  # 替换为你要爬取的网址
    html = get_html_content(url)
    soup = BeautifulSoup(html, 'html.parser')
    print(html)

    element = soup.select_one('html > body > div.container > section:nth-child(4) > div > table > tbody > tr:nth-child(4) > td:nth-child(2)')

    if element:
        text = element.text
        print(text)

        parsed_url = urlparse(text)
        params = parse_qs(parsed_url.query)
        rand_value = params.get('rand', [''])[0]
        print("随机值为:", rand_value)

        clash_url = f"https://wanshanziwo.eu.org/clash/proxies?c=CN,HK,SG,TW,US&type=ss,ssr,vmess,trojan,vless,wireguard&acl=true&rand={rand_value}"
        airport_url = f"https://wanshanziwo.eu.org/airport?core=clash&rand={rand_value}"
        print(clash_url)
        print(airport_url)

        response_clash = requests.get(clash_url, headers=headers)
        clash = response_clash.text
        print('clash.text:', clash[:10])
        if clash.startswith('#'):
            file_path = 'clash.txt'
            write_to_file(file_path, clash)
        time.sleep(5)

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36,Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36'
        }
        response_airport = requests.get(airport_url, headers=headers)
        airport = response_airport.text
        print('airport.text:', airport[:10])
        if airport.startswith('#'):
            file_path = 'clash_airport.txt'
            write_to_file(file_path, airport)
    else:
        print('Element not found.')

scrape_website()
