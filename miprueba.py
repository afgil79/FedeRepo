import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x300")

frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

label_x = tk.Label(frame, text="Texto en eje X")
label_x.pack(side="top", padx=10, pady=10)

# label_y = tk.Label(frame, text="Texto en eje Y", angle=90) # no se puede "rotate" en tkinter
#label_y.pack(side="left", padx=10, pady=10)

canvas_1_manage = tk.Canvas(frame, width = 12, height = 50)
#canvas_1_manage.grid(row = 0, column = 0)
canvas_1_manage.create_text(6, 50, text = "Martin!", angle = 90, anchor = "w")
canvas_1_manage.pack()

root.mainloop()
