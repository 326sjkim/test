
import os
import time, datetime

import pyautogui

def logout():
    return os.system("shutdown -l")

def restart():
    return os.system("shutdown /r /t 10")

def shutdown():
    return os.system("shutdown /s /t 10")


hour=0 ; minute = 0 ; second = 5 

PowerOffTime = hour*3600+minute*60+second ;

Hour = 0 ; Hour_R = 0 ; Minute = 0 ; Minute_R = 0 
PresentTime = time.strftime
dt_now = datetime.datetime.now()
# d_today = datetime.date.today()

Hour = PowerOffTime // 3600
Hour_R = PowerOffTime - Hour * 3600
Minute = Hour_R // 60
Minute_R = Hour_R - Minute * 60



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

shutdown()    
    






    
    








