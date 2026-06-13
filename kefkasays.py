import tkinter as tk


window = tk.Tk()
window.title('Is this a sim?')
window.geometry('450x650')

l = tk.Label(window, bg='white', width=50, font=("Arial", 20), text='click any checkbox to initialize')
l.pack()

def print_selection():
    full_string = ""

    if spread.get() == 1:
        full_string += "SPREAD\n"
    else:
        full_string += "STACK\n"

    if motion.get() == 1:
        full_string += "MOTION\n\n"
    else:
        full_string += "STILLNESS\n\n"

    if g1.get() == 1:
        full_string += "GAZE #1: LOOK IN\n"
    else:
        full_string += "GAZE #1: LOOK OUT\n"

    if g2.get() == 1:
        full_string += "GAZE #2: LOOK IN\n\n"
    else:
        full_string += "GAZE #2: LOOK OUT\n\n"

    if water.get() == 1:
        full_string += "WATER: CIRCLE\n"
    else:
        full_string += "WATER: DONUT\n"

    if fire.get() == 1:
        full_string += "FIRE: DONUT"
    else:
        full_string += "FIRE: CIRCLE"
    """
    if thunder.get() == 1:
        full_string += "THUNDER: FALSE\n"
    else:
        full_string += "THUNDER: TRUE\n"
    if ice.get() == 1:
        full_string += "ICE: FALSE"
    else:
        full_string += "ICE: TRUE"
    """
    l.config(text=full_string)

g1 = tk.IntVar()
g2 = tk.IntVar()
spread = tk.IntVar()
motion = tk.IntVar()
fire = tk.IntVar()
water = tk.IntVar()

thunder = tk.IntVar()
ice = tk.IntVar()

c1 = tk.Checkbutton(window, text='? FIRST GAZE', font=("Arial", 20), variable=g1, onvalue=1, offvalue=0, command=print_selection)
c1.pack(pady=(20, 0))
c2 = tk.Checkbutton(window, text='? SECOND GAZE', font=("Arial", 20), variable=g2, onvalue=1, offvalue=0, command=print_selection)
c2.pack(pady=(0, 20))

c6 = tk.Checkbutton(window, text='? WATER', font=("Arial", 20), variable=water, onvalue=1, offvalue=0, command=print_selection)
c6.pack()
c5 = tk.Checkbutton(window, text='? FIRE', font=("Arial", 20), variable=fire, onvalue=1, offvalue=0, command=print_selection)
c5.pack(pady=(0, 20))

c3 = tk.Checkbutton(window, text='SPREAD', font=("Arial", 20), variable=spread, onvalue=1, offvalue=0, command=print_selection)
c3.pack()
c4 = tk.Checkbutton(window, text='MOTION', font=("Arial", 20), variable=motion, onvalue=1, offvalue=0, command=print_selection)
c4.pack()
"""
c7 = tk.Checkbutton(window, text='? THUNDER',variable=thunder, onvalue=1, offvalue=0, command=print_selection)
c7.pack()
c8 = tk.Checkbutton(window, text='? ICE',variable=ice, onvalue=1, offvalue=0, command=print_selection)
c8.pack()
"""


window.mainloop()