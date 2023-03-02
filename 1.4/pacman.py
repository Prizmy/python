import math
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


def func(x, y):
    cl = (0.1 - (x - 0.5) ** 2 - (y - 0.5) ** 2)*100
    cl = cl * -(0.003 - (x - 0.6) ** 2 - (y - 0.3) ** 2)
    cl = cl * (((y >= 0.5) * ((x - y) < 0)) + ((y < 0.5) * ((x + y) <= 1)))
    return cl * 100 ** 2, cl * 100 ** 2, 0
    

label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2)
label.pack()
label.config(image=img)
tk.mainloop()
