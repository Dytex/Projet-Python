from tkinter import *

fenetre = Tk()

canvas = Canvas(fenetre, width=150, height=120, background='yellow')
txt = canvas.create_text(75, 60, text="Start", font="Arial 16 italic", fill="blue")
canvas.pack()
fenetre.mainloop()