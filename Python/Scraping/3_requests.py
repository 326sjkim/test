''' 
1 교시. 
웹페이지(url) 접속해서(requests.get), 제대로 반응하는지 확인(res.raise_for_statud(), res.status_code 200)
정상인지, requests.codes.ok, 아닌지 확인하고
문서 길이 출력하고, html로 작성(filepoint.write)해본다. 

1 교시 2)
코드를 바로 돌리면 자동으로 __name__을 __main__으로 할당한다. 
'''

import requests

def main():
    # python 3에서는 print() 으로 사용합니다.
    
    #res = requests.get("http://naver.com")
    res = requests.get("http://google.com")
    res.raise_for_status()
    print("응답코드 : ", res.status_code)  # 200이면 정상, 다른값이면 비정상

    if res.status_code == requests.codes.ok:
        print("정상입니다.")
    else:  # else:
        print("문제 발생. [에러코드 : ", res.status_code, "]")

    print("test")
    print(len(res.text))
    # print(res.text)

    with open("./scraping/mygoogle.html", "w", encoding="utf8") as f:
        f.write(res.text)

if __name__ == "__main__":
	main()

