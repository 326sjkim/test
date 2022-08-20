""" 
11교시.
1. 다음에서 영화 정보 가져오기 - 년도별로 인기 5위까지 영화 가져오기. 
역대 관객 순위 클릭, 역대, 2020, 2019, ... 
https://search.daum.net/search?w=tot&    q=2020     %EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR
<a href= ~~> 
    <img class="thumb_img" src=~~ >
</a>

1. url부터 체크 : 클릭했을 때, url이 어떻게 변하는지 확인한다.
2. 세번이나 클릭해야 이미지를 저장할 수 있다. 
3. url 정보를 가져와서 붙여넣기 한다.

11-2교시. 
페이지에 있는 링크를 다시 클릭해서 정보 가져오기.

"""

''' 
package and module : import package.module
import package_name
from . import operation   현재 패키지에서 opoeration 모듈을 가지고 옴
__init__.py : 1) 폴더가 패키지로 인식되도록 함. 2) 패키지를 초기화

패키지만 가져오면
어느 패키지의 어느 모듈을 사용할지 정확하게 명시.

import requests
res = requests.get()

from package import *  # package의 모든 변수, 함수, 클래스 가져옴
module : 변수, 함수, 클래스 파일   (filename.py)
package : 여러 모듈을 묶은 것      (폴더 : namespace, 이름공간)
라이브러리(표준 라이브러리) :       (기본으로 설치된 모듈과 패키지)

import package.module
import package.module1, package.module2
package.module.variable
package.module.function()
package.module.class()

import urllib.request
response = urllib.request.urlopen('http://google.co.kr')

import hello
def he()
    ~~~
    
hello.hi()

import로 모듈을 가져오면 해당 스크립트 파일이 한 번 실행됩니다. 
따라서 hello 모듈을 가져오면 hello.py 안의 코드가 실행됩니다.
이때 __name__이라는 변수에는 hello를 임포트해오기 때문에, 
hello.py의 __name__ 변수에는 'hello'가 들어가고, main.py의 __name__ 변수에는 '__main__'이 들어갑니다.

결론.
파일을 모듈로 사용할수도 있고, 그냥 독립적인 실행코드로 쓸수도 있다.
독립적인 실행코드로 쓸려면 if __name__="__name__":

'''

import requests
from bs4 import BeautifulSoup

import os  # 폴더 생성할라고

# 폴더 생성하기
def createFolder(folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
    except OSError:
        print('Error: Creating folder. ' + folder)

if __name__ == "__main__":
    # folder = "./scraping/data"   # 현재 작업 폴더는 MyStock
    foldername = './data'
    createFolder(foldername)

    # for image in images:
    #     print(image)
    #     # 결과 : <img alt="" class="thumb_img" height="164" is-person-img="false" \
    #     # src="//search1.kakaocdn.net/thumb/R232x328.q85/?fname=http%3A%2F%2Ft1.daumcdn.net \
    #     # %2Fmovie%2F5afd212b68e34e61a964d969dd898e2f1574298873981" width="116"/>

    # 다른언어 : for, foreach, for of 파이썬 : for in 한가지만 제공한다. iterable : 반복가능한 객체
    # for item in iterable ( collection.iterable에 속한 instance)
    # import collections : list, dict, set, string, bytes, tuple, range : dict는 key:value중 key가 i로 들어간다.
    # range(5) , range(0, 5) -> 0, 1, ~ ,4
    # for i in var_list
    # enumerate함수 : 반복문 사용할 때, 몇번째 반복문인지 확인하고자 할 때, 인덱스 번호와 원소를 tuple형태로 반환 (idx, 원소)

    for year in range(2015, 2021):

        url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')

        images = soup.find_all("img", attrs={"class": "thumb_img"})

        for idx, image in enumerate(images):
            #    print(idx, image["src"])
            image_url = image["src"]
            if image_url.startswith("//"):                # //로 시작하면 https:를 붙인다.
                image_url = "https:" + image_url
            print(image_url)

            image_res = requests.get(image_url)  # 이 페이지에
            image_res.raise_for_status()

            # 이미지 다 가져오기
            
            with open(foldername+"/movie_{}_{}.jpg".format(year, idx+1), "wb") as f:
                f.write(image_res.content)

            if idx >= 7:  # 1위부터 10위까지만 하고 탈출
                break
        # end for idx, image
    # end for year
