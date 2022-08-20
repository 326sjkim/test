"""
 2교시. 정규식 연습
"""
""" ex
주민등록번호 : 901201-111111
이메일주소  : nadocoding@gmail.com 
차량번호 : 11가 1234, 123가 4567
IP 주소 : 192.168.0.1 # 1000.1111.2121.1111 # X
"""

# ca?e
import re  # regular expression
p = re.compile("ca.e")   # p: pattern
"""
1) . : 하나의 문자 
2) ^ : 문자열의 시작 (^de)  : de로 시작하는 문자 > desk, destination,
3) $ : 문자열의 끝 (se$) : se로 끝나는 문자 > case, base

사용예제 :  m = p.match("case") : O,  m=p.match("caffe") : X
"""

def print_match(m):   # 함수
    # print(m.group())   # 처음부터 매치가 되지 않으면 에러가 발생, casetest도 된다.
    if m:
        print("m.group() : ", m.group())  # 일치하는 문자열 반환
        print("m.string() : ", m.string)  # 입력받은 문자열
        print("m.start() : ", m.start())  # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())  # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())  # 일치하는 문자열의 시작과 끝 index
    else:
        print("매칭되지 않음")

m = p.match("case")
print_match(m)

m = p.match("good care")
print_match(m)

lst = p.findall("good care cafe")  # 일치하는 모든 것을 리스트로
print(lst)

# m = p.match("caffe")
# print_match(m)

# m = p.search("good care") # 주어진 문장려중에 일치하는게 있는지 확인
# print_match(m)

""" 사용하는 형태
1. p = re.compile("원하는형태")
2. m = p.match("비교할 문자열")
3. m = p.search("비교할 문자열")
4. lst = p.findall("찾을 문자열") 을 리스트로 만들어준다.
참고. w2shcool. Python Regfx
google 검색키워드 : python re
"""
