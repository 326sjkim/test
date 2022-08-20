''' 
Project) 나만의 웹스크래핑을 이용하여 나만의 비서를 만드시오.

1. 네이버에서 날씨 정보가져오기
2. 네이버 뉴스홈에서 최근 세개정도 링크를 같이 가져오기
3. IT/과학 에서 뉴스 3개정도 가져오기
4. 해커스 어학원에서 한글지문, 영어지문 가져와서 잘 번역했는지 하자.


[출력 예시]
[오늘의 날씨] - naver
흐림, 어제보다 00° 높아요 
현재 00°C (최저 00° / 최고 00 ) 
오전 강수확률 00% / 오후 강수확률 00%

미세먼지 001/좋음. 
초미세먼지 0018/좋음

[헤드라인 뉴스] | - naver
1. 무슨 무슨 일이...
(링크 : https://...) 
2. 어떤 어떤 일이...
(링크 : https://...) 
3. 이런 저런 일이 ... 
(링크 : https://...)

[IT 뉴스] - naver
1. 무슨 무슨 일이...
(링크 : https://...) 
2. 어떤 어떤 일이 ...
(링크 : https://...) 
3. 이런 저런 일이 ... 
(링크 : https://...)

[오늘의 영어 회화] - hackers
(영어 지문) 
Jason : How do you think bla bla..? 
Kim : Well, I think ...
(한글 지문) 
Json : 어쩌구 저쩌구 어떻게 생각하세요? 
Kim : 글쎄요, 저는 어쩌구 저쩌구

위 정보을 이메일이나 메신저로 보내면 된다.

'''

import enum
import requests
from bs4  import BeautifulSoup
import re


# 흐림, 어제보다 00° 높아요 
# 현재 00°C (최저 00° / 최고 00 ) 
# 오전 강수확률 00% / 오후 강수확률 00%

# 미세먼지 001/좋음. 
# 초미세먼지 0018/좋음 '''

def create_soup(url):
    
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml') 
    
    return soup

def print_news(index, title, link):
    print(f'{index+1}.{title}')
    print(f"링크 : {link}")
    
    
def scrape_weather():
    print('오늘 날씨 & 내일 날씨')  
    
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98+%EB%82%A0%EC%94%A8&tqi=h6PyxdprvmZssecw4WCssssssqs-137244'
    soup = create_soup(url)
    cast = soup.find('p', attrs={'class':'cast_txt'}).get_text()
    curr_temp = soup.find("p", attrs={'class':'info_temperature'}).get_text().replace("도씨","")
    min_temp = soup.find("span", attrs={'class':'min'}).get_text()
    max_temp = soup.find("span", attrs={'class':'max'}).get_text()
    
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    # "class":["리스트를 사용해도 된다.","리스트"]
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text() # 미세먼지    
    pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지

    #출력
    print(cast)
    print(f"현재 {curr_temp} (최저{min_temp} / 최고 {max_temp})")
    print()
    print(f"미세먼지 {pm10}")
    print(f"초미세먼지 {pm25}")
    print()
    
def scrape_headline_news():
    print('헤드라인 뉴스')
    url = 'https://news.naver.com/'
        
    soup = create_soup(url)
    
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all('li', limit=3)
    for index, news in enumerate(news_list):
        
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx=1
         
        a_tag = news.find_all("a")[a_idx]    
        title = a_tag.get_text().strip()
        link = a_tag["href"]
        
        print_news(index,title, link)

    print()
        
      
def scrape_english():
     
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english'
    
    soup = create_soup(url)
    #sentences = soup.find_all('div', id=attrs={"id":re.compile("^conv_kor_t")})
    # sentences = soup.select_one('')    
    sentences = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})
    
    # print(sentences)
    
    # for 지정한 인덱스부터 : 끝까지
    print('[영어지문]')
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text(strip=True))
        
    print('[한글지문]')        
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text(strip=True))
    
    # sentences = soup.select('div')
    # 문장 갯수가 몇개인지 모른다.
    #for sentence in sentences[len(sentences)//2]:  # 예를 들어 가져올 문장의 반은 한글먼저/ 영어
    #    sen = sentence.get_text() 
        
      
        
    

if __name__ == '__main__':
    # scrape_weather()
    # scrape_headline_news()
    
    scrape_english()
   
