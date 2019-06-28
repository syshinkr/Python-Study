import tkinter as tk
from tkinter import font
import threading
import serial

root = tk.Tk()
root.title("스마트 홈")

tempList = []
humiList = []

ser = serial.Serial(
    port='COM3',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1)


def display_sensor(ser):
    while True:
        rxdata = ser.readline().decode('utf-8')
        if rxdata:
            print(rxdata)
            temp_d = rxdata[2:6]
            # print(temp_d)
            humi_d = rxdata[10:14]
            # print(humi_d)
            tempList.append(temp_d)
            humiList.append(humi_d)

thread = threading.Thread(target=display_sensor, args=(ser,))
thread.start()
root.mainloop()
