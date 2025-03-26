import pyautogui as pg
import time
import keyboard
import cv2 as cv


while True:
    try:
        img = pg.locateOnScreen('target.png', confidence=0.8, grayscale = True)
        print('Found it!')
    except:
        pass
    pg.moveTo(img)
    
    pg.click()
    time.sleep(0.1)
    if(keyboard.is_pressed('q')):
        print("Out of Program")
        break