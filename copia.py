# Use para dar "ctrl v" em td texto que vc der 'ctrl c' quantas vezes quiser!

import pyautogui, time
time.sleep(4)
for i in range(50):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press("enter")
    time.sleep(3)

