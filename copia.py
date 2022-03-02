import pyautogui, time,keyboard
time.sleep(3)
while true:
    while keyboard.is_pressed('2') == False:
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press("enter")
 
