import tkinter as tk
from tkinter import font
import threading
import serial

root = tk.Tk()
root.title("스마트 홈")

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
        if rxdata :
          print(rxdata)
          temp_d = rxdata[2:6]
          humi_d=rxdata[10:14]
          lux_d=rxdata[18:22]
          cnvs.create_rectangle(180, 170, 300, 210, width=3, fill='white', outline='#11aaaa')
          cnvs.create_rectangle(400, 170, 520, 210, width=3, fill='white', outline='#11aaaa')
          cnvs.create_rectangle(180, 340, 300, 340, width=3, fill='white', outline='#11aaaa')
          cnvs.create_text((210, 190), anchor=tk.W, fill='Black', font=('Helvetica', -27, 'bold'), text=temp_d)
          cnvs.create_text((440, 190), anchor=tk.W, fill='Black', font=('Helvetica', -27, 'bold'), text=humi_d)
          cnvs.create_text((210, 400), anchor=tk.W, fill='Black', font=('Helvetica', -27, 'bold'), text=lux_d)


cnvs = tk.Canvas(width = 800, height = 480)
cnvs.config(bg = 'White')
cnvs.grid(column=0, row=0)
cnvs.create_rectangle((0, 0, 800, 100), fill = '#aaccaa', outline = '#333399')
cnvs.create_text((120, 50), anchor=tk.W, fill='#3311ff', font=('Helvetica', -40, 'bold'), text='Smart Home Air Quality Monitor')

cnvs.create_text((200, 150), anchor=tk.W, fill='Black', font=('Helvetica', -30, 'bold'), text='Temp')
cnvs.create_rectangle(180, 170, 300, 210, width=3, fill='white', outline='#11aaaa')

cnvs.create_text((430, 150), anchor=tk.W, fill='Black', font=('Helvetica', -30, 'bold'), text='Humi')
cnvs.create_rectangle(400, 170, 520, 210, width=3, fill='white', outline='#11aaaa')

cnvs.create_text((200, 300), anchor=tk.W, fill='Black', font=('Helvetica', -30, 'bold'), text='Lux')
cnvs.create_rectangle(180, 340, 300, 340, width=3, fill='white', outline='#11aaaa')

thread = threading.Thread(target=display_sensor, args=(ser,))
thread.start()
root.mainloop()
