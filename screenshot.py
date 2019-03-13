import pyautogui
import time

x=1
while True:
	pyautogui.screenshot("C:\screenshots\image"+str(x)+".png")
	x+=1
	time.sleep(5)