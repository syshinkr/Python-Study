import tkinter as tk

#TODO : import 에러나는데 실행은 됨
import pygame

pygame.init()
pygame.mixer.init()

def click1():
    sounda = pygame.mixer.Sound('wav/pig.wav')
    sounda.play()

def click2():
    soundb = pygame.mixer.Sound('wav/cat.wav')
    soundb.play()

def click3():
    soundc = pygame.mixer.Sound('wav/bird.wav')
    soundc.play()

def click4():
    soundd = pygame.mixer.Sound('wav/wolf.wav')
    soundd.play()

root = tk.Tk()
frame1 = tk.Frame(root, width=800, height=480)
frame1.pack(side=tk.TOP, fill=tk.X)
photo1 = tk.PhotoImage(file="image/pig250x200.png")
button1 = tk.Button(frame1, width=250, height=200, image=photo1, command=click1)
button1.grid(row=0, column=0)
photo2 = tk.PhotoImage(file="image/CAT250x200.png")
button2 = tk.Button(frame1, width=250, height=200, image=photo2, command=click2)
button2.grid(row=0, column=1)
photo3 = tk.PhotoImage(file="image/bird250x200.png")
button3 = tk.Button(frame1, width=250, height=200, image=photo3, command=click3)
button3.grid(row=1, column=0)
photo4 = tk.PhotoImage(file="image/wolf250x200.png")
button4 = tk.Button(frame1, width=250, height=200, image=photo4, command=click4)
button4.grid(row=1, column=1)
root.mainloop()
