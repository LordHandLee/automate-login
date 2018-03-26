from tkinter import *
from tkinter import ttk
#from PIL import Image, ImageTk
from PIL import Image, ImageTk
import psutil
import win32gui
import win32process
import win32con
import time
import subprocess
import pyautogui
#from functions import *
import fileinput


pyautogui.FAILSAFE = False

global WoW_Count
global set
global PID
PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
WoW_Count = 0
set = 0




def doNothing():
    print("ok ok I won't...")


def get_hwnds(pid):
    """return a list of window handlers based on it process id"""
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
            if found_pid == pid:
                hwnds.append(hwnd)
        return True
    hwnds = []
    win32gui.EnumWindows(callback, hwnds)
    return (hwnds)

def openWoW():
        open = subprocess.Popen("F:\Ethan's Desktop\File folders\World of Warcraft 1.12\WoW.exe")
        open


def wow_start():
    hwnd = get_hwnds(PID[0])
    hwnd1 = get_hwnds(PID[1])
    hwnd2 = get_hwnds(PID[2])
    hwnd3 = get_hwnds(PID[3])
    hwnd4 = get_hwnds(PID[4])
    hwnd5 = get_hwnds(PID[5])
    hwnd6 = get_hwnds(PID[6])
    hwnd7 = get_hwnds(PID[7])
    hwnd8 = get_hwnds(PID[8])
    hwnd9 = get_hwnds(PID[9])
    win32gui.ShowWindow(hwnd[0], win32con.SW_RESTORE)
    win32gui.MoveWindow(hwnd[0], -10, 0, 399, 540, True)
    win32gui.SetActiveWindow(hwnd[0])
    # time.sleep(2)
    win32gui.ShowWindow(hwnd1[0], win32con.SW_RESTORE)
    win32gui.MoveWindow(hwnd1[0], 374, 0, 399, 540, True)
    win32gui.SetActiveWindow(hwnd1[0])
    # time.sleep(2)
    win32gui.ShowWindow(hwnd2[0], win32con.SW_RESTORE)
    win32gui.SetActiveWindow(hwnd2[0])
    win32gui.MoveWindow(hwnd2[0], 759, 0, 399, 540, True)
    # time.sleep
    win32gui.ShowWindow(hwnd3[0], win32con.SW_RESTORE)
    win32gui.SetActiveWindow(hwnd3[0])
    win32gui.MoveWindow(hwnd3[0], 1143, 0, 399, 540, True)
    # time.sleep
    win32gui.ShowWindow(hwnd4[0], win32con.SW_RESTORE)
    win32gui.SetActiveWindow(hwnd4[0])
    win32gui.MoveWindow(hwnd4[0], 1528, 0, 399, 540, True)
    # time.sleep
    win32gui.ShowWindow(hwnd5[0], win32con.SW_RESTORE)
    win32gui.MoveWindow(hwnd5[0], -10, 533, 399, 540, True)
    win32gui.SetActiveWindow(hwnd5[0])
    # time.sleep(2)
    win32gui.ShowWindow(hwnd6[0], win32con.SW_RESTORE)
    win32gui.MoveWindow(hwnd6[0], 374, 533, 399, 540, True)
    win32gui.SetActiveWindow(hwnd6[0])
    # time.sleep(2)
    win32gui.ShowWindow(hwnd7[0], win32con.SW_RESTORE)
    win32gui.SetActiveWindow(hwnd7[0])
    win32gui.MoveWindow(hwnd7[0], 759, 533, 399, 540, True)
    # time.sleep
    win32gui.ShowWindow(hwnd8[0], win32con.SW_RESTORE)
    win32gui.SetActiveWindow(hwnd8[0])
    win32gui.MoveWindow(hwnd8[0], 1143, 533, 399, 540, True)
    # time.sleep
    win32gui.ShowWindow(hwnd9[0], win32con.SW_RESTORE)
    win32gui.SetActiveWindow(hwnd9[0])
    win32gui.MoveWindow(hwnd9[0], 1528, 533, 399, 540, True)

def login():
    """logs in all accounts for given rotation"""
    #for set in set
    username = 'Lordhandlee'
    password = 'ehl23837'
    hwnd = get_hwnds(PID[0])
    hwnd1 = get_hwnds(PID[1])
    hwnd2 = get_hwnds(PID[2])
    hwnd3 = get_hwnds(PID[3])
    hwnd4 = get_hwnds(PID[4])
    hwnd5 = get_hwnds(PID[5])
    hwnd6 = get_hwnds(PID[6])
    hwnd7 = get_hwnds(PID[7])
    hwnd8 = get_hwnds(PID[8])
    hwnd9 = get_hwnds(PID[9])
    accounts = [hwnd[0], hwnd1[0], hwnd2[0], hwnd3[0], hwnd4[0], hwnd5[0], hwnd6[0], hwnd7[0], hwnd8[0], hwnd9[0]]
    for number in accounts:
        win32gui.ShowWindow(number, win32con.SW_RESTORE)
        win32gui.SetActiveWindow(number)
        win32gui.SetForegroundWindow(number)
        pyautogui.typewrite(username)
        pyautogui.press('tab')
        pyautogui.typewrite(password)
        pyautogui.press('enter')

def help_login(filename, filename1):
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    with open(filename1, "r") as p:
        lines2 = p.read().splitlines()
    line = list(lines)
    line2 = list(lines2)
    accounts = [get_hwnds(PID[x])[0] for x in range(10)]
    for n in lines:
        line = list(lines)
        username = n
    for i in lines2:
        line2 = list(lines2)
        password = i
    for number in accounts:
        # enumerate_object = enumerate(lines)
        # iteration = next(enumerate_object)
        win32gui.ShowWindow(number, win32con.SW_RESTORE)
        win32gui.SetActiveWindow(number)
        win32gui.SetForegroundWindow(number)
        pyautogui.typewrite(username)
        pyautogui.press('tab')
        pyautogui.typewrite(password)
        pyautogui.press('enter')
        # print(next(iter(username)))
        # print(next(iter(password)))
        print(line)
        print(username)
        print(password)

def login1():
    """logs in all accounts for given rotation"""

    if set == 0:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[0:9]:
            lines = list(lines)
            username = n
        for i in lines2[0:9]:
            lines2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
                    print(lines)
                    print(lines2)

    if set == 1:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[10:19]:
            line = list(lines)
            username = n
        for i in lines2[10:19]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)

    if set == 2:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[20:29]:
            line = list(lines)
            username = n
        for i in lines2[20:29]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 3:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[30:39]:
            line = list(lines)
            username = n
        for i in lines2[30:39]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 4:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[40:49]:
            line = list(lines)
            username = n
        for i in lines2[40:49]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 5:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[50:59]:
            line = list(lines)
            username = n
        for i in lines2[50:59]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 6:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[60:69]:
            line = list(lines)
            username = n
        for i in lines2[60:69]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 7:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[70:79]:
            line = list(lines)
            username = n
        for i in lines2[70:79]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 8:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[80:89]:
            line = list(lines)
            username = n
        for i in lines2[80:89]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 9:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[90:99]:
            line = list(lines)
            username = n
        for i in lines2[90:99]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 10:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[100:109]:
            line = list(lines)
            username = n
        for i in lines2[100:109]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 11:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[110:119]:
            line = list(lines)
            username = n
        for i in lines2[110:119]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 12:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[120:129]:
            line = list(lines)
            username = n
        for i in lines2[120:129]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 13:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[130:139]:
            line = list(lines)
            username = n
        for i in lines2[130:139]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 14:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[140:149]:
            line = list(lines)
            username = n
        for i in lines2[140:149]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 15:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[150:159]:
            line = list(lines)
            username = n
        for i in lines2[150:159]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 16:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[160:169]:
            line = list(lines)
            username = n
        for i in lines2[160:169]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 18:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[180:189]:
            line = list(lines)
            username = n
        for i in lines2[180:189]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 19:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[190:199]:
            line = list(lines)
            username = n
        for i in lines2[190:199]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 20:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[200:209]:
            line = list(lines)
            username = n
        for i in lines2[200:209]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 21:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[210:219]:
            line = list(lines)
            username = n
        for i in lines2[210:219]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 22:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[220:229]:
            line = list(lines)
            username = n
        for i in lines2[220:229]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)
    if set == 23:
        with open("accountnames.txt", "r") as f:
            lines = f.read().splitlines()
        with open("passwords.txt", "r") as p:
            lines2 = p.read().splitlines()
        line = list(lines)
        line2 = list(lines2)
        accounts = [get_hwnds(PID[x])[0] for x in range(10)]
        for n in lines[230:239]:
            line = list(lines)
            username = n
        for i in lines2[230:239]:
            line2 = list(lines2)
            password = i
        for number in accounts:
                    #enumerate_object = enumerate(lines)
                    #iteration = next(enumerate_object)
                    win32gui.ShowWindow(number, win32con.SW_RESTORE)
                    win32gui.SetActiveWindow(number)
                    win32gui.SetForegroundWindow(number)
                    pyautogui.typewrite(username)
                    pyautogui.press('tab')
                    pyautogui.typewrite(password)
                    pyautogui.press('enter')
                    #print(next(iter(username)))
                    #print(next(iter(password)))
                    print(username)
                    print(password)

def testlogin(name):
    if testlogin(name):
        print("name")
    if testlogin(name2):
        print("name2")
    else:
        print('else')


def killWoW():
    for  proc in psutil.process_iter():
        if proc.name() == 'WoW.exe':
            proc.kill()

def start():
    WoW_Count = 0
    set = 0
    global PID
    PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
    while WoW_Count < 10 and set < 24:
        prog = ttk.Progressbar(root, style="red.Horizontal.TProgressbar", orient='horizontal', length=500, mode='determinate', maximum=10, val=start())
        prog.start(interval=None)
        openWoW()
        WoW_Count += 1
        prog.update()
        if WoW_Count >= 10:
            username = "Lordhandlee"
            password = 'ehl23837'
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login()
            time.sleep(5)
            #prog.stop()
            #timenow = time.time()
            #elapsed = timenow - time.time()
            #if elapsed >= 70:

            killWoW()
            WoW_Count = 0
            set += 1
            while set == 1 and WoW_Count < 10:
                    openWoW()
                    WoW_Count += 1
                    time.sleep(5)
                    wow_start()
            if set == 2 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 3 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 4 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 5 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 6 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 7 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 8 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 9 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 10 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 11 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 12 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 13 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 14 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 15 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 16 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 17 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 18 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 19 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 20 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 21 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 22 and WoW_Count < 10:
                    openWoW()
                    wow_start()
            if set == 23 and WoW_Count < 10:
                    openWoW()
                    wow_start()
                    set = 0

def start1():
    WoW_Count = 0
    set = 0
    global PID
    PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
    while WoW_Count < 10 and set == 0:
            openWoW()
            WoW_Count += 1
            if WoW_Count >= 10:
                time.sleep(3)
                PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
                wow_start()
                time.sleep(5)
                login()
                time.sleep(10)
                killWoW()
                set = set + 1
            continue


    while WoW_Count < 10 and set == 1:
            openWoW()
            WoW_Count += 1
            if WoW_Count >= 10:
                time.sleep(3)
                PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
                wow_start()
                time.sleep(5)
                login()
                time.sleep(10)
                killWoW()
                set = set + 1

def start2():
    WoW_Count = 0
    set = 0
    global PID
    PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
    while WoW_Count < 10:
        if set == 0:
          openWoW()
          WoW_Count += 1
        if WoW_Count >= 10:
            time.sleep(3)
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            wow_start()
            time.sleep(5)
            login()
            time.sleep(5)
            killWoW()
            WoW_Count = 0
            set += 1
        if set == 1:
            openWoW()
            WoW_Count += 1
        if WoW_Count >=10:
            time.sleep(3)
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            wow_start()
            time.sleep(5)
            login()
            time.sleep(5)
            killWoW()
            WoW_Count = 0
            set += 1
        if set == 2:
            openWoW()
            WoW_Count += 1
        if WoW_Count >=10:
            time.sleep(3)
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            wow_start()
            time.sleep(5)
            login()
            time.sleep(5)
            killWoW()
            WoW_Count = 0
            set += 1
        if set == 3:
            openWoW()
            WoW_Count += 1
        if WoW_Count >=10:
            time.sleep(3)
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            wow_start()
            time.sleep(5)
            login()
            time.sleep(5)
            killWoW()
            WoW_Count = 0
            set += 1
        if set == 4:
            openWoW()
            WoW_Count += 1
        if WoW_Count >=10:
            time.sleep(3)
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            wow_start()
            time.sleep(5)
            login()
            time.sleep(5)
            killWoW()
            WoW_Count = 0
            set += 1


def openWoW2():
    count = 9
    open = subprocess.Popen("F:\Ethan's Desktop\File folders\World of Warcraft 1.12\WoW.exe")
    for i in range(count):
        open = subprocess.Popen("F:\Ethan's Desktop\File folders\World of Warcraft 1.12\WoW.exe")
        open

def start3():
    global set
    set = 0
    set1 = 1
    #count = 9
    count1 = 1
    WoW_Count = 0
    global PID
    PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
    while True:
        PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
        if set == 0:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 1:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 2:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 3:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 4:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 5:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 6:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 7:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 8:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 9:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 10:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 11:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 12:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 13:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 14:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 15:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 16:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 17:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 18:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 19:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 20:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 21:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 22:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1
        if set == 23:
            openWoW2()
            PID = [x.pid for x in psutil.process_iter() if x.name() == "WoW.exe"]
            time.sleep(3)
            wow_start()
            time.sleep(3)
            login1()
            time.sleep(3)
            killWoW()
            set += 1



def start4():
    login(name2)














root = Tk()
root.title("World of Warcraft Automation")
root.geometry("800x600+500+300")
root.resizable(0,0)
root.configure(background='black')
#root.overrideredirect(True)



icon = ImageTk.PhotoImage(Image.open(r"C:\Users\leeet\Desktop\WoW_icon.png"))
root.tk.call('wm', 'iconphoto', root._w, icon)
#image = Image.open(r"C:\Users\leeet\Desktop\WoW_icon.png")
#photo = PhotoImage(image)
##label.pack(side = "bottom", fill = "both", expand = "yes")

#root.iconbitmap(r'C:\Users\leeet\Desktop\maxresdefault.jpg')

btn = Button(root, text="Start", command=start3)
btn.pack()
#btn.grid(column=3, row=1)

s = ttk.Style()
s.theme_use('clam')
s.configure("red.Horizontal.TProgressbar", foreground='blue', background='blue')

'''Progress Bar'''
prog = ttk.Progressbar(root, style="red.Horizontal.TProgressbar", orient='horizontal',length=500,mode='determinate', maximum=10) #value= , variable=)
#prog.pack()
prog.start(interval=5)
#q = prog.stop()
#prog.grid(column=3, row=2)
prog.pack()

q = prog.stop()
btn1 = Button(root, text="progressbar", command=prog.start)
btn1.pack()
#btn1.grid(column=2, row=2)

btn2 = Button(root, text="stopprogressbar", command=prog.stop)
#btn2.grid(column=2, row=1)
btn2.pack()


def open_top():
    global top1
    global top_button
    z = 0
    top1 = Toplevel(root, bg="black")
    top1.title("Groups of Accounts")
    top1.geometry("600x800")

def leftClick(event):
    print("Left")

def leftClick2(event):
    print("Left")



top_button = Button(root, text="Accounts", command=open_top)
top_button.bind("<Button-1>", leftClick2)
# top_button.grid(column=1, row=1)
top_button.pack()

class FetusGod(top_button):
    def __init__(self, master=None, **kwargs):
        Button.__init__(self, master, **kwargs)
        self.config(command=self.toggle)

    def toggle(self):
        self.config(command=self['None'])

global z
z = 0

if z == 0:
    top_button.destroy()
    top_button = Button(root, text="Accounts", command=open_top())
    top_button.bind("<Button-1>", leftClick2)
    top_button.pack()
    # top_button.grid(column=1, row=1)
    top_button.configure(state='active')


    root.update()
    z = 1

if z >= 1:
    top_button.destroy()
    top_button = Button(root, text="Accounts", command=None)
    top_button.bind("<Button-1>", leftClick2)
    top_button.pack()
    # top_button.grid(column=1, row=1)
    #top_button.configure(state='disabled')

    root.update()

    z = 0

def leftClick(event):
    print("Left")
    # if leftClick(top_button):
    #     z = "crap"
    # else:
    #     z = "shit"


def leftClick1(event):
    print("Left")

def leftClick2(event):
    print("Left")

'''New Window'''

def quit():
    top1.destroy()

'''account entry'''
def account_entry(top2):
    global username1, username2, username3, username4, username5, username6, username7, username8, username9, username10, password1, password2, password3, password4, password5, password6, password7, password8, password9, password10
    global btn3
    username1 = StringVar()
    e = Entry(top2, textvariable=username1)
    e.grid(row=0, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password1)
    e1.grid(row=0, column=3)

    username2 = StringVar()
    e = Entry(top2, textvariable=username2)
    e.grid(row=1, column=1)

    password2 = StringVar()
    e1 = Entry(top2, textvariable=password2)
    e1.grid(row=1, column=3)

    username3 = StringVar()
    e = Entry(top2, textvariable=username3)
    e.grid(row=2, column=1)

    password3 = StringVar()
    e1 = Entry(top2, textvariable=password3)
    e1.grid(row=2, column=3)

    username4 = StringVar()
    e = Entry(top2, textvariable=username4)
    e.grid(row=3, column=1)

    password4 = StringVar()
    e1 = Entry(top2, textvariable=password4)
    e1.grid(row=3, column=3)

    username5 = StringVar()
    e = Entry(top2, textvariable=username5)
    e.grid(row=4, column=1)

    password5 = StringVar()
    e1 = Entry(top2, textvariable=password5)
    e1.grid(row=4, column=3)

    username6 = StringVar()
    e = Entry(top2, textvariable=username6)
    e.grid(row=5, column=1)

    password6 = StringVar()
    e1 = Entry(top2, textvariable=password6)
    e1.grid(row=5, column=3)

    username7 = StringVar()
    e = Entry(top2, textvariable=username7)
    e.grid(row=6, column=1)

    password7 = StringVar()
    e1 = Entry(top2, textvariable=password7)
    e1.grid(row=6, column=3)

    username8 = StringVar()
    e = Entry(top2, textvariable=username8)
    e.grid(row=7, column=1)

    password8 = StringVar()
    e1 = Entry(top2, textvariable=password8)
    e1.grid(row=7, column=3)

    username9 = StringVar()
    e = Entry(top2, textvariable=username9)
    e.grid(row=8, column=1)

    password9 = StringVar()
    e1 = Entry(top2, textvariable=password9)
    e1.grid(row=8, column=3)

    username10 = StringVar()
    e = Entry(top2, textvariable=username10)
    e.grid(row=9, column=1)

    password10 = StringVar()
    e1 = Entry(top2, textvariable=password10)
    e1.grid(row=9, column=3)

    '''save buttons'''
    btn3 = Button(top2, text="Save Username 1", command=lambda: save_username_test("accountnames.txt"))
    btn3.bind("<Button-1>", leftClick)
    btn3.grid(column=2, row=0)


    btn4 = Button(top2, text="Save Password 1", command=lambda: save_password("passwords.txt"))
    btn4.bind("Button-1>", leftClick1)
    btn4.grid(column=4, row=0)

    btn5 = Button(top2, text="Save Username 2", command=lambda: save_username("accountnames.txt"))
    btn5.bind("<Button-1>", leftClick)
    btn5.grid(column=2, row=1)


    btn6 = Button(top2, text="Save Password 2", command=lambda: save_password("passwords.txt"))
    btn6.bind("Button-1>", leftClick1)
    btn6.grid(column=4, row=1)

    btn7 = Button(top2, text="Save Username 3", command=lambda: save_username("accountnames.txt"))
    btn7.bind("<Button-1>", leftClick)
    btn7.grid(column=2, row=2)


    btn8 = Button(top2, text="Save Password 3", command=lambda: save_password("passwords.txt"))
    btn8.bind("Button-1>", leftClick1)
    btn8.grid(column=4, row=2)

    btn9 = Button(top2, text="Save Username 4", command=lambda: save_username("accountnames.txt"))
    btn9.bind("<Button-1>", leftClick)
    btn9.grid(column=2, row=3)


    btn10 = Button(top2, text="Save Password 4", command=lambda: save_password("passwords.txt"))
    btn10.bind("Button-1>", leftClick1)
    btn10.grid(column=4, row=3)

    btn11 = Button(top2, text="Save Username 5", command=lambda: save_username("accountnames.txt"))
    btn11.bind("<Button-1>", leftClick)
    btn11.grid(column=2, row=4)


    btn12 = Button(top2, text="Save Password 5", command=lambda: save_password("passwords.txt"))
    btn12.bind("Button-1>", leftClick1)
    btn12.grid(column=4, row=4)

    btn13 = Button(top2, text="Save Username 6", command=lambda: save_username("accountnames.txt"))
    btn13.bind("<Button-1>", leftClick)
    btn13.grid(column=2, row=5)


    btn14 = Button(top2, text="Save Password 6", command=lambda: save_password("passwords.txt"))
    btn14.bind("Button-1>", leftClick1)
    btn14.grid(column=4, row=5)

    btn15 = Button(top2, text="Save Username 7", command=lambda: save_username("accountnames.txt"))
    btn15.bind("<Button-1>", leftClick)
    btn15.grid(column=2, row=6)


    btn16 = Button(top2, text="Save Password 7", command=lambda: save_password("passwords.txt"))
    btn16.bind("Button-1>", leftClick1)
    btn16.grid(column=4, row=6)

    btn17 = Button(top2, text="Save Username 8", command=lambda: save_username("accountnames.txt"))
    btn17.bind("<Button-1>", leftClick)
    btn17.grid(column=2, row=7)


    btn18 = Button(top2, text="Save Password 8", command=lambda: save_password("passwords.txt"))
    btn18.bind("Button-1>", leftClick1)
    btn18.grid(column=4, row=7)

    btn19 = Button(top2, text="Save Username 9", command=lambda: save_username("accountnames.txt"))
    btn19.bind("<Button-1>", leftClick)
    btn19.grid(column=2, row=8)


    btn20 = Button(top2, text="Save Password 9", command=lambda: save_password("passwords.txt"))
    btn20.bind("Button-1>", leftClick1)
    btn20.grid(column=4, row=8)

    btn21 = Button(top2, text="Save Username 10", command=lambda: save_username_test("accountnames.txt"))
    btn21.bind("<Button-1>", leftClick)
    btn21.grid(column=2, row=9)


    btn22 = Button(top2, text="Save Password 10", command=lambda: save_password("passwords.txt"))
    btn22.bind("Button-1>", leftClick1)
    btn22.grid(column=4, row=9)

    return username1, username2, username3, username4, username5, username6, username7, username8, username9, username10, password1, password2, password3, password4, password5, password6, password7, password8, password9, password10

def account_entry2(top2, username1, password1, a, b, c, d):

    username1 = StringVar()
    e = Entry(top2, textvariable=username1)
    e.grid(row=a, column=b)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password1)
    e1.grid(row=c, column=d)

    username1 = StringVar()
    e = Entry(top2, textvariable=username2)
    e.grid(row=1, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password2)
    e1.grid(row=1, column=3)

    username1 = StringVar()
    e = Entry(top2, textvariable=username3)
    e.grid(row=2, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password3)
    e1.grid(row=2, column=3)

    username1 = StringVar()
    e = Entry(top2, textvariable=username4)
    e.grid(row=3, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password4)
    e1.grid(row=3, column=3)

    username1 = StringVar()
    e = Entry(top2, textvariable=username5)
    e.grid(row=4, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password5)
    e1.grid(row=4, column=3)

    username1 = StringVar()
    e = Entry(top2, textvariable=username6)
    e.grid(row=5, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password6)
    e1.grid(row=5, column=3)

    username1 = StringVar()
    e = Entry(top2, textvariable=username7)
    e.grid(row=6, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password7)
    e1.grid(row=6, column=3)

    username1 = StringVar()
    e = Entry(top2, textvariable=username8)
    e.grid(row=7, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password8)
    e1.grid(row=7, column=3)

    username1 = StringVar()
    e = Entry(top2, textvariable=username9)
    e.grid(row=8, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password9)
    e1.grid(row=8, column=3)

    username1 = StringVar()
    e = Entry(top2, textvariable=username10)
    e.grid(row=9, column=1)

    password1 = StringVar()
    e1 = Entry(top2, textvariable=password10)
    e1.grid(row=9, column=3)

    '''save buttons'''
    btn3 = Button(top2, text="Save Username 1", command=lambda: save_username_test("accountnames.txt"))
    btn3.bind("<Button-1>", leftClick)
    btn3.grid(column=2, row=0)

    btn4 = Button(top2, text="Save Password 1", command=lambda: save_password("passwords.txt"))
    btn4.bind("Button-1>", leftClick1)
    btn4.grid(column=4, row=1)



'''New Window'''
def open_top2():
    global top2
    global big
    top2 = Toplevel(root, bg="Black")
    big = top2
    top2.title("Group 1")
    top2.geometry("500x400")
    account_entry(top2)
   #handler = top_button.destroy()
    #top_button = Button(root, text="Close", command=handler)
    #top_button.bind("<Button-1>", leftClick)
    #top_button.pack()
    #Top_Button.grid(column=2, row=0)
    return big
    #account_entry2(top2, username1, password1, 0, 1, 0, 3)

def open_top3():
    global top3
    top3 = Toplevel(root, bg="black")
    top3.title("Group 2")
    top3.geometry("500x400")
    account_entry(top3)
    return top3

def open_top4():
    global top4
    top4 = Toplevel(root, bg="black")
    top4.title("Group 3")
    top4.geometry("500x400")
    account_entry(top4)

def open_top5():
    global top5
    top5 = Toplevel(root, bg="black")
    top5.title("Group 4")
    top5.geometry("500x400")
    account_entry(top5)

def open_top6():
    global top6
    top6 = Toplevel(root, bg="black")
    top6.title("Group 5")
    top6.geometry("500x400")
    account_entry(top6)

def open_top7():
    global top7
    top7 = Toplevel(root, bg="black")
    top7.title("Group 6")
    top7.geometry("500x400")
    account_entry(top7)

def open_top8():
    global top8
    top8 = Toplevel(root, bg="black")
    top8.title("Group 7")
    top8.geometry("500x400")
    account_entry(top8)

def open_top9():
    global top3
    top9 = Toplevel(root, bg="black")
    top9.title("Group 8")
    top9.geometry("500x400")
    account_entry(top9)

def open_top10():
    global top10
    top10 = Toplevel(root, bg="black")
    top10.title("Group 9")
    top10.geometry("500x400")
    account_entry(top10)

def open_top11():
    global top11
    top11 = Toplevel(root, bg="black")
    top11.title("Group 10")
    top11.geometry("500x400")
    account_entry(top11)

def open_top12():
    global top12
    top12 = Toplevel(root, bg="black")
    top12.title("Group 11")
    top12.geometry("500x400")
    account_entry(top12)

def open_top13():
    global top13
    top13 = Toplevel(root, bg="black")
    top13.title("Group 12")
    top13.geometry("500x400")
    account_entry(top13)

def open_top14():
    global top14
    top14 = Toplevel(root, bg="black")
    top14.title("Group 13")
    top14.geometry("500x400")
    account_entry(top14)

def open_top15():
    global top15
    top15 = Toplevel(root, bg="black")
    top15.title("Group 14")
    top15.geometry("500x400")
    account_entry(top15)

def open_top16():
    global top16
    top16 = Toplevel(root, bg="black")
    top16.title("Group 15")
    top16.geometry("500x400")
    account_entry(top16)

def open_top17():
    global top17
    top17 = Toplevel(root, bg="black")
    top17.title("Group 16")
    top17.geometry("500x400")
    account_entry(top17)

def open_top18():
    global top18
    top18 = Toplevel(root, bg="black")
    top18.title("Group 17")
    top18.geometry("500x400")
    account_entry(top18)

def open_top19():
    global top19
    top19 = Toplevel(root, bg="black")
    top19.title("Group 18")
    top19.geometry("500x400")
    account_entry(top19)

def open_top20():
    global top20
    top20 = Toplevel(root, bg="black")
    top20.title("Group 19")
    top20.geometry("500x400")
    account_entry(top20)

def open_top21():
    global top21
    top21 = Toplevel(root, bg="black")
    top21.title("Group 20")
    top21.geometry("500x400")
    account_entry(top21)

def open_top22():
    global top22
    top22 = Toplevel(root, bg="black")
    top22.title("Group 21")
    top22.geometry("500x400")
    account_entry(top22)

def open_top23():
    global top23
    top23 = Toplevel(root, bg="black")
    top23.title("Group 22")
    top23.geometry("500x400")
    account_entry(top23)

def open_top24():
    global top24
    top24 = Toplevel(root, bg="black")
    top24.title("Group 23")
    top24.geometry("500x400")
    account_entry(top24)

def open_top25():
    global top25
    top25 = Toplevel(root, bg="black")
    top25.title("Group 24")
    top25.geometry("500x400")
    account_entry(top25)

count = 0

def open_top():
        global top1
        global top_button
        z = 0
        top1 = Toplevel(root, bg="black")
        top1.title("Groups of Accounts")
        top1.geometry("600x800")



        '''Groups'''
        group1 = Button(top1, text="Group 1", bg="red", command=open_top2)
        group1.bind("<Button-1>", leftClick)
        group1.grid(row=1, column=1)

        group2 = Button(top1, text="Group 2", bg="red", command=open_top3)
        group2.bind("<Button-1>", leftClick)
        group2.grid(row=2, column=1)

        group3 = Button(top1, text="Group 3", bg="red", command=open_top4)
        group3.bind("<Button-1>", leftClick)
        group3.grid(row=3, column=1)

        group4 = Button(top1, text="Group 4", bg="red", command=open_top5)
        group4.bind("<Button-1>", leftClick)
        group4.grid(row=4, column=1)

        group5 = Button(top1, text="Group 5", bg="red", command=open_top6)
        group5.bind("<Button-1>", leftClick)
        group5.grid(row=5, column=1)

        group6 = Button(top1, text="Group 6", bg="red", command=open_top7)
        group6.bind("<Button-1>", leftClick)
        group6.grid(row=6, column=1)

        group7 = Button(top1, text="Group 7", bg="red", command=open_top8)
        group7.bind("<Button-1>", leftClick)
        group7.grid(row=7, column=1)

        group8 = Button(top1, text="Group 8", bg="red", command=open_top9)
        group8.bind("<Button-1>", leftClick)
        group8.grid(row=8, column=1)

        group9 = Button(top1, text="Group 9", bg="red", command=open_top10)
        group9.bind("<Button-1>", leftClick)
        group9.grid(row=9, column=1)

        group10 = Button(top1, text="Group 10", bg="red", command=open_top11)
        group10.bind("<Button-1>", leftClick)
        group10.grid(row=10, column=1)

        group11 = Button(top1, text="Group 11", bg="red", command=open_top12)
        group11.bind("<Button-1>", leftClick)
        group11.grid(row=11, column=1)

        group12 = Button(top1, text="Group 12", bg="red", command=open_top13)
        group12.bind("<Button-1>", leftClick)
        group12.grid(row=12, column=1)

        group13 = Button(top1, text="Group 13", bg="red", command=open_top14)
        group13.bind("<Button-1>", leftClick)
        group13.grid(row=1, column=2)

        group14 = Button(top1, text="Group 14", bg="red", command=open_top15)
        group14.bind("<Button-1>", leftClick)
        group14.grid(row=2, column=2)

        group15 = Button(top1, text="Group 15", bg="red", command=open_top16)
        group15.bind("<Button-1>", leftClick)
        group15.grid(row=3, column=2)

        group16 = Button(top1, text="Group 16", bg="red", command=open_top17)
        group16.bind("<Button-1>", leftClick)
        group16.grid(row=4, column=2)

        group17 = Button(top1, text="Group 17", bg="red", command=open_top18)
        group17.bind("<Button-1>", leftClick)
        group17.grid(row=5, column=2)

        group18 = Button(top1, text="Group 18", bg="red", command=open_top19)
        group18.bind("<Button-1>", leftClick)
        group18.grid(row=6, column=2)

        group19 = Button(top1, text="Group 19", bg="red", command=open_top20)
        group19.bind("<Button-1>", leftClick)
        group19.grid(row=7, column=2)

        group20 = Button(top1, text="Group 20", bg="red", command=open_top21)
        group20.bind("<Button-1>", leftClick)
        group20.grid(row=8, column=2)

        group21 = Button(top1, text="Group 21", bg="red", command=open_top22)
        group21.bind("<Button-1>", leftClick)
        group21.grid(row=9, column=2)

        group22 = Button(top1, text="Group 22", bg="red", command=open_top23)
        group22.bind("<Button-1>", leftClick)
        group22.grid(row=10, column=2)

        group23 = Button(top1, text="Group 23", bg="red", command=open_top24)
        group23.bind("<Button-1>", leftClick)
        group23.grid(row=11, column=2)

        group24 = Button(top1, text="Group 24", bg="red", command=open_top25)
        group24.bind("<Button-1>", leftClick)
        group24.grid(row=12, column=2)



        '''if 10 usernames in accountnames then red to green'''
        with open("accountnames.txt", "rt") as f, open("passwords.txt", "rt") as p:
            value = [x.strip() for x in (list(f.readlines()))]
            value2 = [x.strip() for x in (list(p.readlines()))]
            #for line in value and value2:
        if len(value) >= 10 and len(value2) >= 10:
            group1.destroy()
            group1 = Button(top1, text="Group 1", bg="green", command=open_top2)
            group1.bind("<Button-1>", leftClick)
            group1.grid(row=1, column=1)
            root.update()
            print(len(value))
            print(len(value2))
        if len(value) >= 20 and len(value2) >= 20:
            group2.destroy()
            group2 = Button(top1, text= "Group 2", bg="green", command=open_top3)
            group2.bind("<Button-1>", leftClick)
            group2.grid(row=2, column=1)
        if len(value) >= 30 and len(value2) >= 30:
            group3.destroy()
            group3 = Button(top1, text="Group 3", bg="green", command=open_top4)
            group3.bind("<Button-1>", leftClick)
            group3.grid(row=3, column=1)
        if len(value) >= 40 and len(value2) >= 40:
            group4.destroy()
            group4 = Button(top1, text="Group 4", bg="green", command=open_top5)
            group4.bind("<Button-1>", leftClick)
            group4.grid(row=4, column=1)
        if len(value) >= 50 and len(value2) >= 50:
            group5.destroy()
            group5 = Button(top1, text="Group 5", bg="green", command=open_top6)
            group5.bind("<Button-1>", leftClick)
            group5.grid(row=5, column=1)
        if len(value) >= 60 and len(value2) >= 60:
            group6.destroy()
            group6 = Button(top1, text="Group 6", bg="green", command=open_top7)
            group6.bind("<Button-1>", leftClick)
            group6.grid(row=6, column=1)
        if len(value) >= 70 and len(value2) >= 70:
            group7.destroy()
            group7 = Button(top1, text="Group 7", bg="green", command=open_top8)
            group7.bind("<Button-1>", leftClick)
            group7.grid(row=7, column=1)
        if len(value) >= 80 and len(value2) >= 80:
            group8.destroy()
            group8 = Button(top1, text="Group 8", bg="green", command=open_top9)
            group8.bind("<Button-1>", leftClick)
            group8.grid(row=8, column=1)
        if len(value) >= 90 and len(value2) >= 90:
            group9.destroy()
            group9 = Button(top1, text="Group 9", bg="green", command=open_top10)
            group9.bind("<Button-1>", leftClick)
            group9.grid(row=9, column=1)
        if len(value) >= 100 and len(value2) >= 100:
            group10.destroy()
            group10 = Button(top1, text="Group 10", bg="green", command=open_top11)
            group10.bind("<Button-1>", leftClick)
            group10.grid(row=10, column=1)
        if len(value) >= 110 and len(value2) >= 110:
            group11.destroy()
            group11 = Button(top1, text="Group 11", bg="green", command=open_top12)
            group11.bind("<Button-1>", leftClick)
            group11.grid(row=11, column=1)
        if len(value) >= 120 and len(value2) >= 120:
            group12.destroy()
            group12 = Button(top1, text="Group 12", bg="green", command=open_top13)
            group12.bind("<Button-1>", leftClick)
            group12.grid(row=12, column=1)
        if len(value) >= 130 and len(value2) >= 130:
            group13.destroy()
            group13 = Button(top1, text="Group 13", bg="green", command=open_top14)
            group13.bind("<Button-1>", leftClick)
            group13.grid(row=1, column=2)
        if len(value) >= 140 and len(value2) >= 140:
            group14.destroy()
            group14 = Button(top1, text="Group 14", bg="green", command=open_top15)
            group14.bind("<Button-1>", leftClick)
            group14.grid(row=2, column=2)
        if len(value) >= 150 and len(value2) >= 150:
            group15.destroy()
            group15 = Button(top1, text="Group 15", bg="green", command=open_top16)
            group15.bind("<Button-1>", leftClick)
            group15.grid(row=3, column=2)
        if len(value) >= 160 and len(value2) >= 160:
            group16.destroy()
            group16 = Button(top1, text="Group 16", bg="green", command=open_top17)
            group16.bind("<Button-1>", leftClick)
            group16.grid(row=4, column=2)
        if len(value) >= 170 and len(value2) >= 170:
            group17.destroy()
            group17 = Button(top1, text="Group 17", bg="green", command=open_top18)
            group17.bind("<Button-1>", leftClick)
            group17.grid(row=5, column=2)
        if len(value) >= 180 and len(value2) >= 180:
            group18.destroy()
            group18 = Button(top1, text="Group 18", bg="green", command=open_top19)
            group18.bind("<Button-1>", leftClick)
            group18.grid(row=6, column=2)
        if len(value) >= 190 and len(value2) >= 190:
            group19.destroy()
            group19 = Button(top1, text="Group 19", bg="green", command=open_top20)
            group19.bind("<Button-1>", leftClick)
            group19.grid(row=7, column=2)
        if len(value) >= 200 and len(value2) >= 200:
            group20.destroy()
            group20 = Button(top1, text="Group 20", bg="green", command=open_top21)
            group20.bind("<Button-1>", leftClick)
            group20.grid(row=8, column=2)
        if len(value) >= 210 and len(value2) >= 210:
            group21.destroy()
            group21 = Button(top1, text="Group 21", bg="green", command=open_top22)
            group21.bind("<Button-1>", leftClick)
            group21.grid(row=9, column=2)
        if len(value) >= 220 and len(value2) >= 220:
            group22.destroy()
            group22 = Button(top1, text="Group 22", bg="green", command=open_top23)
            group22.bind("<Button-1>", leftClick)
            group22.grid(row=10, column=2)
        if len(value) >= 230 and len(value2) >= 230:
            group23.destroy()
            group23 = Button(top1, text="Group 23", bg="green", command=open_top24)
            group23.bind("<Button-1>", leftClick)
            group23.grid(row=11, column=2)
        if len(value) >= 240 and len(value2) >= 240:
            group24.destroy()
            group24 = Button(top1, text="Group 24", bg="green", command=open_top25)
            group24.bind("<Button-1>", leftClick)
            group24.grid(row=12, column=2)






#def






'''get all usernames and password from files and stores into list'''

#all_usernames = [username1, ]
#all_passwords =


def leftClick(event):
    print("Left")

def leftClick1(event):
    print("Left")
count = 0
def save_username(filename):
    with open(filename, "w+") as f:
            count1 = 0
            lines = f.readline()
            if username1:
                f.write(username1.get() + '\n')
                count1 += 1
            if username2:
                f.write(username2.get() + '\n')
                count1 += 1
            if username3:
                f.write(username3.get() + '\n')
                count1 += 1
            if username4:
                f.write(username4.get() + '\n')
                count1 += 1
            if username5:
                f.write(username5.get() + '\n')
                count1 += 1
            if username6:
                f.write(username6.get() + '\n')
                count1 += 1
            if username7:
                f.write(username7.get() + '\n')
                count1 += 1
            if username8:
                f.write(username8.get() + '\n')
                count1 += 1
            if username9:
                f.write(username9.get() + '\n')
                count1 += 1
            if username10:
                f.write(username10.get() + '\n')
                count1 += 1
            if 'a, b' in len(lines[9]):
                if username1:
                    #f.seek(9)
                    f.write[9](username1.get() + '\n')
                    count1 += 1
                if username2:
                    f.write(username2.get() + '\n')
                    count1 += 1
                if username3:
                    f.write(username3.get() + '\n')
                    count1 += 1
                if username4:
                    f.write(username4.get() + '\n')
                    count1 += 1
                if username5:
                    f.write(username5.get() + '\n')
                    count1 += 1
                if username6:
                    f.write(username6.get() + '\n')
                    count1 += 1
                if username7:
                    f.write(username7.get() + '\n')
                    count1 += 1
                if username8:
                    f.write(username8.get() + '\n')
                    count1 += 1
                if username9:
                    f.write(username9.get() + '\n')
                    count1 += 1
                if username10:
                    f.write(username10.get() + '\n')
                    count1 += 1

def save_username_test(filename):
    with open(filename, "w+") as f:
            count1 = 0
            list1 = [""] * 240
            lines = f.readline()
            #if top2:
            if username1:
                list1[0] = username1.get() + '\n'
                count1 += 1
            if username2:
                list1[1] = username2.get() + '\n'
                count1 += 1
            if username3:
                list1[2] = username3.get() + '\n'
                count1 += 1
            if username4:
                list1[3] = username4.get() + '\n'
                count1 += 1
            if username5:
                list1[4] = username5.get() + '\n'
                count1 += 1
            if username6:
                list1[5] = username6.get() + '\n'
                count1 += 1
            if username7:
                list1[6] = username7.get() + '\n'
                count1 += 1
            if username8:
                list1[7] = username8.get() + '\n'
                count1 += 1
            if username9:
                list1[8] = username9.get() + '\n'
                count1 += 1
            if username10:
                list1[9] = username10.get() + '\n'
                count1 += 1
            for x in list1:
                    #x.strip()
                    #f.write(str(x) + '\n')
                    #f.write("%s%s\n" % str(x))
                    #f.write("\n".join(map(lambda x: str(x), list1)) + "\n")
                    #f.write("\n".join("%s%s" % (str(x) for x in list1)))
                    #f.write("%s%s\n" % (x, x.join(list1)))
                    f.writelines(x)
            root.update()
                #if leftClick(username1)
            #if top3:


def save_password(filename):
    with open(filename, "w+") as f:
            count2 = 0
            if password1:
                f.write(password1.get() + '\n')
                count2 += 1
            if password2:
                f.write(password2.get() + '\n')
                count2 += 1
            if password3:
                f.write(password3.get() + '\n')
                count2 += 1
            if password4:
                f.write(password4.get() + '\n')
                count2 += 1
            if password5:
                f.write(password5.get() + '\n')
                count2 += 1
            if password6:
                f.write(password6.get() + '\n')
                count2 += 1
            if password7:
                f.write(password7.get() + '\n')
                count2 += 1
            if password8:
                f.write(password8.get() + '\n')
                count2 += 1
            if password9:
                f.write(password9.get() + '\n')
                count2 += 1
            if password10:
                f.write(password10.get() + '\n')
                count2 += 1










root.mainloop()
