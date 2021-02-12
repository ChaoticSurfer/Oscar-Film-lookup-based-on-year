import tkinter as tk
from film import get_film_year


def show_entry_fields():
    t = get_film_year(e1.get())
    print(f"film -> {t}")
    v.set(f"film  -> {t}")


master = tk.Tk()
tk.Label(master,
         text="input year").grid(row=0)

v = tk.StringVar()
tk.Label(master, textvariable=v).grid(row=2)



e1 = tk.Entry(master)

e1.grid(row=0, column=1)

tk.Button(master,
          text='Show oscar film', command=show_entry_fields).grid(row=3,
                                                                  column=1,
                                                                  sticky=tk.W,
                                                                  pady=4)

tk.mainloop()
