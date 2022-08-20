''' 
1교시 : 윈도우사이즈 출력하기
'''
import os
import datetime, time
import math

import pyautogui  

# 색정보 가져오기 : pip install pillow

'''
size = pyautogui.size()
print(size)
# size[0] : width
# size[1] : height
'''
 
''' 
2교시 : 마우스 움직이기

#절대좌표 이동
#pyautogui.moveTo(100,900) # 이동
#pyautogui.moveTo(100,1000,duration=3)  # 시간동안 이동

#상대좌표 이동
pyautogui.moveTo(100,900) # 절대 좌표 이동
pyautogui.move(100, 100, duration = 1) # 상대 좌표 이동
print(pyautogui.position())
'''

'''
3교시 : 마우스 클릭 액션

pyautogui.sleep(3)
pyautogui.click()  # pyautogui.mouseDown() # pyautogui.mouseUp() # pyautogui.doubleClick()

pyautogui.click(clicks=500)
p = pyautogui.position()  # p.x p[0]  p.y = [1]
# pyautogui.middleClick() # 휠 클릭  # 

# 타이틀바 잡아서 드래그
# pyautogui.drag(상대좌표.x, 상대좌표.y, duration = 0.25) 
# pyautogui.dragTo() # 절대좌표

pyautogui.scroll() # + : 양수, - : 음수 : 위로
'''

''' 
4교시 : 마우스 정보

pyautogui.mouseInfo()
# #802,363 80,100,60 #50643C 마우스 정보로 가져오기
pyautogui.PAUSE = 1 # 잠시 멈춤
'''

def logout():
    return os.system("shutdown -l")

def restart():
    return os.system("shutdown /r /t 10")

def shutdown():
    return os.system("shutdown /s /t 10")


hour=0 ; minute = 0 ; second = 10 

PowerOffTime = hour*3600+minute*60+second ;

Hour = 0 ; Hour_R = 0 ; Minute = 0 ; Minute_R = 0 
PresentTime = time.strftime
dt_now = datetime.datetime.now()
# d_today = datetime.date.today()

Hour = PowerOffTime // 3600
Hour_R = PowerOffTime - Hour * 3600
Minute = Hour_R // 60
Minute_R = Hour_R - Minute * 60

# print(f"{Hour}시간 {Minute} 분 {Minute_R}초")

# pyautogui.moveTo(2645, 25)
# pyautogui.click(duration=0.25)

f = open(r'd:\Myworkspace\Python\rpa_basic\log.txt','a')
f.writelines('\n'+dt_now.strftime('%Y-%m-%d %H:%M:%S') + f" => 총 시간 : {Hour}시간 {Minute} 분 {Minute_R}초\n")

while(PowerOffTime):
    PowerOffTime = PowerOffTime - 1   
    if(PowerOffTime % 2 == 0) :
        f.writelines(dt_now.strftime('%Y-%m-%d %H:%M:%S') + f' => {PowerOffTime}\n')
    time.sleep(1)
    

f.writelines(dt_now.strftime('%Y-%m-%d %H:%M:%S') + f"\n------  종료 --------\n")

pyautogui.moveTo(2027, 123, duration=1)
pyautogui.click(duration=0.25)

pyautogui.moveTo(2650, 22, duration=1)
pyautogui.click(duration=0.25)

# shutdown()    
    


# quit()메서드로 Python 프로그램 종료
# exit()메서드로 Python 프로그램 종료
# sys.exit()메서드로 Python 프로그램 종료
# os.exit()메서드로 Python 프로그램 종료



'''
5교시 : 스크린 샷
# img = pyautogui.screenshot()
# img.save('test.png')
'''






    
    








