import time
import webbrowser
import os
import subprocess
import pyautogui


def chooseWindow(x, y):
    pyautogui.click(151, 1053)        # click on task viwe buton
    time.sleep(1)
    pyautogui.click(x, y)             # click desktop no.



time.sleep(5)

# ------------------------------DESKTOP 3---------------------------------------------------

chooseWindow(555, 91)               # click on desktop 3
time.sleep(2)
os.system('start OneNote:')          # open onenote


# ------------------------------DESKTOP 1---------------------------------------------------


chooseWindow(137, 79)                                        # move to desktop 1
time.sleep(2) 
webbrowser.open("https://mail.google.com/mail/u/1/#inbox")   # open work mail
time.sleep(5)
webbrowser.open("https://www.zenclass.in/class")               # open ZEN class web page
time.sleep(8)
# pyautogui.click(1805, 195)                                         # logout   
# time.sleep(2)
# pyautogui.click(1680, 555)                                         # logout   
# time.sleep(5)
# pyautogui.click(1626, 213)                                         # login
# time.sleep(8)
# pyautogui.click(1270, 802)                                           # signin !!!
# time.sleep(5)
pyautogui.click(45, 364)                                     # go to codekata
time.sleep(3)
webbrowser.open("https://www.guvi.in/ide")               # open GUVI ide page
time.sleep(8)
pyautogui.click(688, 247)                                     # pseudo-click
time.sleep(1)
pyautogui.click(688, 247)                                     # Select programming language
time.sleep(2)
pyautogui.click(687, 718)                                     # Select JavaScript
time.sleep(2)
pyautogui.moveTo(165, 281) 
time.sleep(1)
f = open("D://Coding//GUVI//codetemplate.txt", 'r', encoding="utf-8")
code_template = f.read()                   
pyautogui.dragTo(739, 944)                                    # select the text
time.sleep(1)
pyautogui.write(code_template, interval = 0.10)                                                   # paste the text from onenote


# ------------------------------DESKTOP 2---------------------------------------------------


chooseWindow(378, 89)           # move to desktop 2
# To open an app that is not inbuilt in windows, use subprocess.call('file location')
subprocess.call('C://Users//iloke//AppData//Roaming//Zoom//bin//Zoom.exe')    # open zoom


# ------------------------test---------------------------------------------------------------
# time.sleep(5)
# print(pyautogui.position())
