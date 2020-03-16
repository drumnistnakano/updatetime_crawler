import sys
import requests

url = sys.argv[1]
r = requests.get(url)
# レスポンスボディのバイト列からエンコーディングを推定
r.encoding = r.apparent_encoding
print(f'encoding: {r.encoding}', file=sys.stderr)
print(r.text)
