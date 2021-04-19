# Usando o arquivo txt para enviar as menssagens:

import pyautogui, time
time.sleep(4)
txt = open("txt", 'r')
for word in txt:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
