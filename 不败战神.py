from bs4 import BeautifulSoup
import requests

def download(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    title = soup.find_all('h2', class_='chapter-title')
    title = title[0].text + ".txt"
    content = soup.find_all('div', class_='article')
    for i in content:
        with open(title, "a",encoding='utf-8') as f:
            print("已下载保存为：" + title)
            f.write(str(i.text))
# 开始爬取
num = input("输入页数")
num = int(num) - 1
url = "https://www.qimao.com/shuku/149774-317"
if num == 0:
    download('https://www.qimao.com/shuku/149774-316193/')
else:
    download('https://www.qimao.com/shuku/149774-316193/')
    for i in range(271,271+num):
        r = requests.get(url + str(i) + "/", timeout=5)
        if r.status_code == 200:
            download(url + str(i) + "/")
        else:
            print("no")