'''
    Author: Riley Anderson
    Date: 21/10/2021
    Description: This is the hangman component of the game
    version: 1.0, basic made
'''

import tkinter as tk
import turtle as t

def draw_me():
    global entry
    number = entry.get()
    draw.pendown()
    if int(number) == 1:
        draw.forward(300)
    elif int(number) == 2:
        draw.right(90)
        draw.forward(150)
    elif int(number) == 3:
        draw.right(90)
        draw.forward(50)
    elif int(number) == 4:
        draw.right(90)
        draw.circle(20)
    elif int(number) == 5:
        draw.left(90)
        draw.penup()
        draw.forward(40)
        draw.pendown()
        draw.forward(70)
    elif int(number) == 6:
        draw.left(45)
        draw.forward(50)
    elif int(number) == 7:
        draw.left(180)
        draw.penup()
        draw.forward(50)
        draw.left(90)
        draw.pendown()
        draw.forward(50)
    elif int(number) == 8:
        draw.penup()
        draw.right(180)
        draw.forward(50)
        draw.left(45)
        draw.forward(40)
        draw.pendown()
        draw.right(135)
        draw.forward(30)
    elif int(number) == 9:
        draw.penup()
        draw.right(180)
        draw.forward(30)
        draw.left(90)
        draw.pendown()
        draw.forward(30)
    elif int(number) == 10:
        draw.penup()
        draw.right(180)
        draw.forward(30)
        draw.left(45)
        draw.forward(60)
        draw.left(90)
        draw.forward(5)
        draw.pendown()
        draw.dot(5, 'black')
        draw.penup()
        draw.left(180)
        draw.forward(10)
        draw.pendown()
        draw.dot(5, 'black')
        draw.penup()
        draw.backward(10)
        draw.right(90)
        draw.forward(20)
        draw.right(90)
        draw.forward(5)
        draw.pendown()
        draw.left(225)
        for x in range(1,15):
            draw.forward(2)
            draw.right(7)
        draw.penup()
        draw.forward(100)
    entry.delete(0)
    
root = tk.Tk()
root.title('Hangman')
root.geometry('1200x1200')

canvas = tk.Canvas(root)
canvas.config(width=600, height=600)
canvas.pack(side=tk.RIGHT)
screen = t.TurtleScreen(canvas)
screen.bgcolor('white')
frame = tk.Frame()
frame.pack(side=tk.LEFT, padx=10)
entry = tk.Entry(frame)
entry.pack()
button = tk.Button(frame, text='hit me', command=draw_me)
button.pack()
draw = t.RawTurtle(screen)
draw.penup()
draw.goto(0,-100)
draw.left(90)
root.mainloop()
