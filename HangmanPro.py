import tkinter
import random
from PIL import Image, ImageTk
from functools import partial


# Loading / Sorting / Resizing Images
def load_images():
    extension = 'png'

    for parts in body_parts:
        name = f"Hangman Pictures/{parts}.{extension}"
        image = (Image.open(name))
        resized_image = image.resize((220, 300), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        picture_names[parts] = new_image


# Code for button click commands
def button_click(letter, r, c):
    global x, y
    used_letters.append(letter)

    # Transfer button clicked to used buttons box

    buttons[letter] = tkinter.Menubutton(used_letters_box, text=letter,
                                         font=letters_font, bg='grey69') \
        .grid(row=y, column=x)

    buttons[letter] = tkinter.Button(letter_box, text='', font='black', bg='black') \
        .grid(row=r, column=c, sticky=stick, padx=(2, 2), pady=(2, 2))

    x += 1

    if x == 3:
        y += 1
        x = 0

    if letter in answer:
        correct_letters(letter)

    else:
        wrong_letters()


# If choice is in the word
def correct_letters(letter):
    global correct

    for index, char in enumerate(answer):
        if letter == char:
            # Place Letter in Correct Slot
            correct_letter_slot[index] = tkinter.Button(correct_letters_slot, text=letter,
                                                        font=correct_letters_font, bg='grey69',
                                                        relief='flat', height=1, width=1) \
                .grid(row=0, column=index)
            correct += 1
        else:
            pass
    if correct == len(answer):
        game_win()


# If choice is not in the word
def wrong_letters():
    global hangman_base, counter
    counter += 1

    if counter > 6:
        return
    else:
        hangman_base.destroy()

        hang_pic = body_parts[counter]

        hangman_base = tkinter.Label(hangman_graphic, image=picture_names[hang_pic])
        hangman_base.grid(sticky='nsew', padx=(5, 0), pady=(12, 0))
        hangman_base.configure(bg='dark turquoise')

        if hang_pic == 'Both Arms':
            main_window.after(500, no_letters)
            main_window.after(3000, game_lose)


def game_lose():
    clear()
    main_window.configure(bg='red')

    final_window = tkinter.LabelFrame(main_window, bg='red', relief='flat')
    final_window.grid(row=0, column=0, rowspan=2)

    game_over = tkinter.Label(final_window, text='Game Over', font=end_game_font, bg='red')
    game_over.grid(row=0, column=0, sticky='news', padx=(140, 0), pady=(80, 0))

    final_buttons_frame = tkinter.LabelFrame(main_window, bg='red', relief='flat')
    final_buttons_frame.grid(row=2, column=0)

    play_again = tkinter.Button(final_buttons_frame, text='Play Again', font=available_font)
    play_again.grid(row=0, column=0, padx=(120, 15), pady=(0, 220))

    answer_display = tkinter.Label(main_window, text=f'The answer is: {answer}',
                                   font=available_font, bg='red', relief='flat')
    answer_display.grid(row=3, column=0)

    exit_game = tkinter.Button(final_buttons_frame, text='   Exit   ', font=available_font, command=end_game)
    exit_game.grid(row=0, column=1, padx=(15, 0), pady=(0, 220))


def game_win():
    clear()
    main_window.configure(bg='green')

    final_window = tkinter.LabelFrame(main_window, bg='green', relief='flat')
    final_window.grid(row=0, column=0, rowspan=2)

    game_over = tkinter.Label(final_window, text='You Win!', font=end_game_font, bg='green')
    game_over.grid(row=0, column=0, sticky='news', padx=(140, 0), pady=(80, 0))

    final_buttons_frame = tkinter.LabelFrame(main_window, bg='green', relief='flat')
    final_buttons_frame.grid(row=2, column=0)

    play_again = tkinter.Button(final_buttons_frame, text='Play Again', font=available_font)
    play_again.grid(row=0, column=0, padx=(120, 15), pady=(0, 220))

    exit_game = tkinter.Button(final_buttons_frame, text='   Exit   ', font=available_font, command=end_game)
    exit_game.grid(row=0, column=1, padx=(15, 0), pady=(0, 220))


def no_letters():
    n_rows = 1
    n_columns = 0
    for char in letters:
        if char in used_letters:
            pass

        else:
            buttons[char] = tkinter.Button(letter_box, text=char, font=letters_font, bg='snow2') \
                .grid(row=n_rows, column=n_columns, sticky=stick, padx=(2, 2), pady=(2, 2))

        n_columns += 1

        if n_columns == 13:
            n_rows += 1
            n_columns = 0


# Selects a random length and word
def word_chooser():
    while True:
        five_letters = (
            "adult", "apple", "beach", "board", "brain", "chest", "death",
            "earth", "fight", "heart", "group", "hotel", "issue", "novel", "range",
        )
        six_letters = (
            "branch", "career", "casual", "coffee", "damage", "dealer", "editor",
            "effect", "ground", "guilty", "latter", "leader", "market", "person", "reward",
        )
        seven_letters = (
            "airline", "western", "village", "warrant", "traffic",
            "trouble", "thought", "surface", "supreme", "request",
            "raining", "reality", "profile", "passing", "monitor",
        )
        eight_letters = (
            "abstract", "activity", "advanced", "colorful", "compound",
            "conflict", "consumer", "disaster", "disposal", "engineer",
            "everyone", "firewall", "hardware", "quizzing", "majority",
        )

        number = random.randint(5, 8)

        separator = ""
        word = [" "] * number

        if number == 5:
            word = random.choice(five_letters)
        elif number == 6:
            word = random.choice(six_letters)
        elif number == 7:
            word = random.choice(seven_letters)
        elif number == 8:
            word = random.choice(eight_letters)

        word = separator.join(word)
        return word.upper()


# Empty contents of main window
def clear():
    trash = main_window.grid_slaves()
    for dump in trash:
        dump.destroy()


def play():
    main_window.mainloop()


def end_game():
    main_window.destroy()


####################################################################
# Lists
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
           'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

body_parts = ['Base', 'Head', 'Body', 'Left Leg',
              'Both Legs', 'Left Arm', 'Both Arms']

####################################################################
# Empty Variables
y, x = 0, 0
counter = 0
correct = 0

####################################################################
# Empty Sets
picture_names = {}
used_letters = []
buttons = {}
letter_slot = {}
correct_letter_slot = {}

####################################################################
# Calling Functions
answer = word_chooser()

####################################################################
# Different Fonts
letters_font = ('Bodoni MT Black', 15, 'bold')
title_font = ('Arial', 15, 'bold')
available_font = ('Rockwell Condensed', 17, 'bold', 'italic')
used_font = ('Arial', 12, 'bold', 'italic', 'underline')
correct_letters_font = ('Bodoni MT Black', 25, 'bold', 'underline')
end_game_font = ('Bodoni MT Black', 75, 'bold')

####################################################################
# Main Window
main_window = tkinter.Tk()
main_window.geometry('950x590+350+150')
main_window['pady'] = 5
main_window['padx'] = 5
main_window.configure(bg='grey69')

####################################################################

# Row Configure
for i in range(0, 4):
    main_window.rowconfigure(i, weight=1)
    if i != 3:
        main_window.columnconfigure(i, weight=1)

####################################################################

# Top Frame and Label
top_title = tkinter.LabelFrame(main_window, bd=0, bg='grey69')
top_title.grid(row=0, column=0, columnspan=3, sticky='new')

for i in range(0, 3):
    top_title.columnconfigure(i, weight=1)

game_title = tkinter.Label(top_title, text="Hangman", font=title_font, bg='grey69')
game_title.grid(row=0, column=1)
####################################################################

# Hangman Box
hangman_graphic = tkinter.LabelFrame(main_window, width=150, bd=15, bg='dark turquoise')
hangman_graphic.grid(row=1, column=0, rowspan=2, sticky='nwse')
hangman_graphic.grid_propagate(0)

# Hangman Pictures
load_images()

hangman_base = tkinter.Label(hangman_graphic, image=picture_names['Base'])
hangman_base.grid(sticky='nsew', padx=(5, 0), pady=(12, 0))
hangman_base.configure(bg='dark turquoise')

####################################################################

# Used Letters Box
used_letters_box = tkinter.LabelFrame(main_window, text="Used Letters", font=used_font, bd=0, bg='grey69')
used_letters_box.configure(height=300, width=100)
used_letters_box.grid(row=1, column=2, rowspan=2, sticky='ns')
used_letters_box.grid_propagate(0)

columns = 0
rows = 0

for i in range(0, len(letters)):
    tkinter.Menubutton(used_letters_box, bg='grey69').grid(column=columns, row=rows)
    rows += 1
    if rows == 13:
        rows = 0
        columns += 1
####################################################################

# Correct Letters
correct_letters_slot = tkinter.Frame(main_window)
correct_letters_slot.grid(row=2, column=1)

rows = 0
columns = 0
for i in range(0, len(answer)):
    letter_slot[i] = tkinter.Button(correct_letters_slot, text='__', font='bold', bg='grey69',
                                    relief='flat', height=3, width=3) \
        .grid(row=rows, column=columns)
    columns += 1

####################################################################

# Bottom Letter Window
letter_box = tkinter.LabelFrame(main_window, bg='snow2')
letter_box.grid(row=4, column=0, columnspan=3, sticky='sew')
letter_box['pady'] = 5

letter_label = tkinter.Label(main_window, text='Available Letters', font=available_font, bg='grey69')
letter_label.grid(row=3, column=0, columnspan=3, sticky='swe')

for i in range(0, 13):
    letter_box.columnconfigure(i, weight=1)
for i in range(0, 3):
    letter_box.rowconfigure(i, weight=1)

rows = 1
columns = 0
stick = 'ew'
v = 1
i = 0
####################################################################

# Assigning letters to the buttons
for let in letters:
    buttons[let] = tkinter.Button(letter_box, text=let, font=letters_font, bg='snow2',
                                  command=partial(button_click, let, rows, columns)) \
        .grid(row=rows, column=columns, sticky=stick, padx=(2, 2), pady=(2, 2))

    columns += 1

    if columns == 13:
        rows += 1
        columns = 0

####################################################################

main_window.minsize(950, 590)
main_window.maxsize(950, 590)

if __name__ == '__main__':
    play()
