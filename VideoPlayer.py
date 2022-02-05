import selenium
from selenium import webdriver
import time
import pyautogui



#Defining Navigator --- In case you don't use chrome you must change the webdriver, but before it you may install the one you want and put it in the same folder of the python script
navegador=webdriver.Chrome()
 

#Opening navigator --- Ps.: In the () down here, please make sure you put the page YOU want to open, otherwise you will hear lofi :)
navegador.get("https://www.youtube.com/c/LofiGirl")


#Acessing the video --- Depending of the position you want to click you may change the coordinates, in order to do it take a look at GetPosition.py in my repository 
pyautogui.click(x=344, y=619)


#Opening Vs code --- You may change the words in () on line 23 so you can open other stuff
time.sleep(2)
pyautogui.press("win")
pyautogui.write("Visual Studio Code")
pyautogui.press("enter")

