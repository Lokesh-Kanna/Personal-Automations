import time
import webbrowser
import os
import subprocess
import pyautogui

previousSession = int(input('What was the previous session number?\n>'))

def waitAndExecute (sec):
    time.sleep(sec)
    pyautogui.press('enter')

def wait(sec):
    time.sleep(sec)

def chooseWindow(x, y):
    pyautogui.click(151, 1053)                                                # click on task viwe buton
    time.sleep(1)
    pyautogui.click(x, y)                                                     # click desktop no.

# ------------------------------DESKTOP 3---------------------------------------------------

chooseWindow(555, 91)                                                         # click on desktop 3
time.sleep(2)
os.system('start OneNote:')                                                   # open onenote

# ------------------------------DESKTOP 1---------------------------------------------------

# Browser Actions
chooseWindow(137, 79)                                                         # move to desktop 1
time.sleep(2) 
webbrowser.open("https://www.zenclass.in/class")                              # open ZEN class web page
time.sleep(8)

# Cmd actions
pyautogui.hotkey('ctrl', 'esc')                                               # Open Start menu
wait(1)
pyautogui.write('powershell', 0.03)                                           # Search powershell
waitAndExecute(1)                                                             # Open Windows PowerShell
wait(4)
pyautogui.write('D:', 0.02)                                                   # Switch to D drive
waitAndExecute(0.5)               
wait(1)
pyautogui.write('cd Coding/GUVI/"Recorded Sessions"/"Main Bootcamp"', 0.02)   # Cd to Main Bootcamp
waitAndExecute(0.5)
wait(2)
pyautogui.write(f'mkdir "Session {previousSession + 1}"', 0.02)               # Make session folder
waitAndExecute(0.5)
wait(1)
pyautogui.write(f"cd 'Session {previousSession + 1}'")                        # Go to session folder
waitAndExecute(0.5)
wait(1)
pyautogui.write(f'mkdir "Session code"', 0.02)                                # Make code folder
waitAndExecute(0.5)
wait(1)
pyautogui.write("cd 'Session code'")                                          # Go to code folder
waitAndExecute(0.5)
wait(1)
pyautogui.write("New-Item index.html -type file", 0.01)                       # Create index.html file 
waitAndExecute(0.5)
wait(1)
pyautogui.write("New-Item script.js -type file", 0.01)                        # Create script.js file
waitAndExecute(0.5)
wait(1)
pyautogui.write("code .", 0.1)                                                # open code folder in vs code
waitAndExecute(0.5)
wait(1)







# time.sleep(5)
# print(pyautogui.position())
