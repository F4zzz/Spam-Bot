import pyautogui, time, keyboard
time.sleep(3)
txt = open("txt", 'r')
for word in txt:
    while keyboard.is_pressed('2') == False:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
