
""" 5교시 : user agent

403에러 피하기, 
google에서 user agent string
what is my User Agent? 검색
https://www.whatismybrowser.com/detect/what-is-my-user-agent
Mozilla/5.0 (Windows NT 10.0; Win64; x64) 
AppleWebKit/537.36 (KHTML, like Gecko) 
Chrome/87.0.4280.66 Safari/537.36
접속하는 브라우저, 컴퓨터에 따라 다르게 나온다.
"""

import requests

url = "http://nadocoding.tistory.com"
#url = "http://naver.com"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"}
    
res = requests.get(url, headers=headers)
# res.raise_for_status()

with open("./scraping/나도코딩.html", "w", encoding="utf-8-sig") as f:
    f.write(res.text)
