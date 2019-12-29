import requests
from bs4 import BeautifulSoup

# ターゲットURL
url = "https://www.city.kasuga.fukuoka.jp/kosodate/ninshin/kyoushitsu/1001479.html"
# クローリング
response = requests.get(url)
# 文字化け防止
response.encoding = response.apparent_encoding

# スクレイピング
bs = BeautifulSoup(response.text, 'html.parser')
bs_p = bs.find('p', class_='update')
print(bs_p.text)
