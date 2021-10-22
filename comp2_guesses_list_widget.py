'''
    Author: Riley Anderson
    Date: 21/10/2021
    Description: This is the section to display the used guesses
    version: 1.0, basic made
'''

import tkinter as tk

def list_change():
    global entry1, label, display_list
    additive = entry1.get()
    print(display_list, additive)
    display_list.append(additive)
    print(display_list)
    print(*display_list, sep=', ')
    label['text'] = display_list
display_list = []    
root = tk.Tk()
root.title('Hangman')
root.geometry('1200x1200')

#---------- Guesses list frame ------------
frame = tk.Frame(root, bg='blue', width=600, height=600)
frame.pack_propagate(0)
frame.pack(side=tk.LEFT, padx=10, anchor='n')
entry1 = tk.Entry(frame)
entry1.pack()
button = tk.Button(frame, text='hit me', command=list_change)
button.pack()
label = tk.Label(frame)
label.pack()
root.mainloop()
