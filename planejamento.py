import pyautogui as pg
import time
import os


def open_drive() :
    os.system("start Chrome.exe")
    time.sleep(2)
    pg.hotkey('win', 'up')
    time.sleep(4)
    pg.write('https://onedrive.com/')
    time.sleep(1)
    pg.press('enter')   
    time.sleep(10)

def planner() :
    open_drive()
    pg.click(645, 127)
    pg.write('planejamento')
    time.sleep(0.5)
    pg.press('enter')
    time.sleep(3)
    pg.click(341, 384)
    time.sleep(5)
    pg.hotkey('ctrl', 'a')
    time.sleep(3)
    pg.click(426, 178)
    


planner()
time.sleep(10)
pg.hotkey('alt', 'f4')