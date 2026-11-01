import requests
from bs4 import BeautifulSoup

# 这是专门给新手练习爬虫的网站，不用担心被抓
url = "http://quotes.toscrape.com/"

print(f"正在偷偷潜入: {url} ...\n")
# 发送网络请求，拿到网页的源代码
response = requests.get(url)

# 如果状态码是 200，说明访问成功
if response.status_code == 200:
    # 把源代码丢给 BeautifulSoup 解析
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 找到所有的名言区块（通过分析网页代码的 class="quote"）
    quotes = soup.find_all('div', class_='quote')
    
    # 把抓到的名言保存到文件里
    with open("quotes.txt", "w", encoding="utf-8") as f:
        for i, quote in enumerate(quotes, 1):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            print(f"{i}. {text} —— {author}")
            
            # 写入 txt 文件
            f.write(f"{i}. {text} —— {author}\n")
            
    print("\n✅ 成功！名言已全部保存到当前目录的 quotes.txt 文件中。")
else:
    print("❌ 潜入失败，网络不通！")