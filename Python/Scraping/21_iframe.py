
# frame 전환
''' 

    <html>
        <body>
            <iframe id="1">
                <html> 
                    <body>
                        <div id>
                    </body>
                </html>
            </iframe>
            <iframe id="2">
                <html> 
                    <body>
                    </body>
                </html>
            </iframe>
        </body>
    </html>
    
iframe으로 구성되어진 html 문서는 xpath를 사용할 수 없다.
최상위 html로 하위 iframe을 검색할 수는 없다.

ex 사이트) w3shcool의 html 실행화면
iframe로 전환하지 않으면 찾아갈수 없다.
    
'''


import time
from selenium import webdriver

browser = webdriver. Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input')
browser.switch_to. frame ('ifremeResult')
elem = browser.find_element_by_xpath('7/*[@id="male"]')
browser.switch_to.default_content()

elem.click()
time.sleep (5)
browser.quit()


