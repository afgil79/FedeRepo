from tkinter import *
ws = Tk()
ws.title(string='')
ws.geometry('400x300')

frame = LabelFrame(ws,text='Hello_World',bg='#f0f0f0', font=(30,14))
frame.pack(expand=True, fill=BOTH)

Button(frame,text='Submit').pack()

ws.mainloop()