import pyautogui
import time
import randfacts

time.sleep(5)

for i in range(200):
    x = randfacts.get_fact()
    pyautogui.typewrite(x)
    pyautogui.typewrite("\n")
    time.sleep(5)
