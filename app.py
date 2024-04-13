from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
import webbrowser

navegador = webdriver.Chrome()
try:
    linkMensagem_whatsapp = 'https://web.whatsapp.com/'
    webbrowser.open(linkMensagem_whatsapp)
except Exception as e:
    print(e)
    seta = pyautogui.locateCenterOnScreen('seta.png')
    sleep(5)
    pyautogui.click(seta)