import sys                                                                                                                                                                    
import requests

# 第一引数:エンコーディング方式を取得したいURL
url = sys.argv[1]
r = requests.get(url)
print(f'encoding : {r.encoding}', file=sys.stderr)
print(r.text)
