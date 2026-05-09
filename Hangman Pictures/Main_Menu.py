"""Tkinter Hangman main menu scaffold (incomplete — for loop body missing)."""
import tkinter


def play():
    menu.mainloop()


title_font = ('Arial', 15, 'bold')


menu = tkinter.Tk()
menu.geometry('950x590+350+150')
menu['pady'] = 5
menu['padx'] = 5


for i in range (0,4):
    menu.rowconfigure(i, weight=1)
    if i != 3:
        menu.columnconfigure(i, weight=1)


title = tkinter.LabelFrame(menu)
title.grid(row=0, column=0, columnspan=3, sticky='new')

for i in range(0, 3):
    pass


title_name = tkinter.Label(title, text="Select a Game", font=title_font)
title_name.grid(row=0, column=0, sticky='w')


menu.minsize(950, 590)
menu.maxsize(950, 590)


if __name__ == '__main__':
    play()
