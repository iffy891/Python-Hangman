'''
    Author: Riley Anderson
    Date: 21/10/2021
    Description: Word display section of widget
    version: 1.0, basic made

'''

import tkinter as tk

fontstyle = ("comic Sans Ms", "80", "bold")
entrystyle = ('comic Sans Ms', '14', 'normal')   
root = tk.Tk()
root.title('Hangman')
width= root.winfo_screenwidth() 
height= root.winfo_screenheight()
root.geometry("%dx%d" % (width, height))
top_frame = tk.Frame(root)
top_frame.pack(side=tk.TOP)
canvas = tk.Canvas(top_frame)
canvas.config(width=700, height=500)
canvas.pack(side=tk.RIGHT, anchor='ne', padx=10)
#screen = t.TurtleScreen(canvas)
screen.bgcolor('white')

#---------- Guesses list frame ------------
frame = tk.Frame(top_frame, bg='blue', width=700, height=500)
frame.pack_propagate(0)
frame.pack(side=tk.LEFT, padx=10, anchor='nw')
'''
entry = tk.Entry(frame)
entry.pack()
'''
entry1 = tk.Entry(frame)
entry1.pack()
button = tk.Button(frame, text='hit me', command=list_change)
button.pack()
label = tk.Label(frame)
label.pack()

bot_frame = tk.Frame(root, width=1300, height=600, bg='red')
bot_frame.pack_propagate(0)
bot_frame.pack(side=tk.BOTTOM, anchor='s')
bot_label = tk.Label(bot_frame, text=' _  _  _  _  _ ', font=fontstyle)
bot_label.place(x=300, y=100)
guess_entry = tk.Entry(bot_frame, width=10, font=entrystyle)
guess_entry.pack(ipadx=10, anchor='n')

'''
draw = t.RawTurtle(screen)
draw.penup()
draw.goto(0,-100)
draw.left(90)
'''
root.mainloop()

