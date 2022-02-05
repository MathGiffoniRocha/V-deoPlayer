import selenium
from selenium import webdriver
import time
import pyautogui



#Definindo navegadorÇ
navegador=webdriver.Chrome()
 

#Abrindo navegador
navegador.get("https://www.youtube.com/c/LofiGirl")


#Acessando o vídeo:
pyautogui.click(x=344, y=619)



#Abrindo o vs code:
pyautogui.press("win")
pyautogui.write("Visual Studio Code")
pyautogui.press("enter")

