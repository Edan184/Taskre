import tkinter as tk
import os, sys
from PIL import Image, ImageTk

class main_application(tk.Frame):
    def __init__(self,parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        
        logo = Image.open('logo.png')
        logo = ImageTk.PhotoImage(logo.resize((750,800)))
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=1, row=0)

        task_pag_inst = tk.Label(root, text="Select a task", font="Raleway")
        task_pag_inst.grid(columnspan=3, column=0, row=1)

        browse_text = tk.StringVar()
        browse_btn = tk.Button(root, textvariable=browse_text, font="Raleway")
        browse_text.set("Browse")
        browse_btn.grid(column=1, row=2)


if __name__ == "__main__":
    root = tk.Tk()
    canvas = tk.Canvas(root, width=100, height=100)
    canvas.grid(columnspan=3, rowspan=3)
    main_application(root)
    root.mainloop()