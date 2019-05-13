from win32api import keybd_event
import tkinter as tk
from tkinter import messagebox
import time,threading,pyttsx3,win32file

def getUsbList():
    drive_list = []
    drivebits=win32file.GetLogicalDrives()
    for d in range(1,26):
        mask=1 << d
        if drivebits & mask:
            # here if the drive is at least there
            drname='%c:\\' % chr(ord('A')+d)
            t=win32file.GetDriveType(drname)
            if t == win32file.DRIVE_REMOVABLE:
                drive_list.append(drname)
    return drive_list

def rotate_screen(orientation):
    vals = dict(zip(['left', 'up', 'right', 'down'],
                    [37, 38, 39, 40])) 
    comb = 165, vals[orientation]
    for k in comb:
        keybd_event(k, 0, 1, 0)
    for k in reversed(comb):
        keybd_event(k, 0, 2, 0)

def spin():
    rotate_screen("right")
    time.sleep(0.5)
    rotate_screen("down")
    time.sleep(0.5)
    rotate_screen("left")
    time.sleep(0.5)
    rotate_screen("up")
    time.sleep(0.5)

def askyesno(title,message):
    root = tk.Tk()
    root.overrideredirect(1)
    root.withdraw()
    return messagebox.askyesno(title, message)

def square(image):
    s=Tk()
    s.geometry("+300+300")
    s.overrideredirect(True)
    s.call('wm', 'attributes', '.', '-topmost', '1')

    i="./images/"+image+".png"
    img=PhotoImage(file=i)

    font=("Arial",50)
    l=Label(s,image=img,font=font)
    l.grid()
    l.bind("<Button-1>",lambda e:s.destroy())

    s.mainloop()
