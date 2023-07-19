from tkinter import *
import random
import pandas as pd

FRENCH_WORD = ""
ENGLISH_WORD = ""
GLOBAL_DICTIONARY = {
    "English": "",
    "French": "",
                     }

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()

# ---------Read CSV--------------
# Use of pandas to read the csv
words_df = pd.read_csv("data/french_words.csv")


def generate_word():
    """This function takes a random word from the dataframe and the respective translation"""
    global flip_timer, ENGLISH_WORD, FRENCH_WORD
    canvas.itemconfig(card_background, image=front_img)
    random_index = random.randint(0, len(words_df["English"].tolist()))
    FRENCH_WORD = words_df.at[random_index, "French"]
    ENGLISH_WORD = words_df.at[random_index, "English"]
    # english_list.append(english_word)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=FRENCH_WORD)
    flip_timer = window.after(3000, func=flipcard)


def flipcard():
    global ENGLISH_WORD
    canvas.itemconfig(card_title, text="English")
    canvas.itemconfig(card_word, text=ENGLISH_WORD)
    canvas.itemconfig(card_background, image=back_img)


def unknown():
    global ENGLISH_WORD, FRENCH_WORD
    generate_word()
    GLOBAL_DICTIONARY["English"] = ENGLISH_WORD
    GLOBAL_DICTIONARY["French"] = FRENCH_WORD
    data = pd.DataFrame(GLOBAL_DICTIONARY)
    data.to_csv("data/words_to_learn.csv")



# ------------GUI-----------------
# Creation of the main screen
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flipcard)

# Creation right and wrong button

right_img = PhotoImage(file="C:/Users/Me/Desktop/Carlos Python Projects/Day 31/images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=generate_word)
right_button.grid(column=2, row=5)

wrong_img = PhotoImage(file="C:/Users/Me/Desktop/Carlos Python Projects/Day 31/images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=unknown)
wrong_button.grid(column=1, row=5)

# Canvas objects for the flash cards

canvas = Canvas(width=800, height=526, highlightthickness=0)
front_img = PhotoImage(file="C:/Users/Me/Desktop/Carlos Python Projects/Day 31/images/card_front.png")
card_background = canvas.create_image(400, 263, image=front_img)
canvas.config(bg=BACKGROUND_COLOR)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 250, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=1, row=0, columnspan=2)

back_img = PhotoImage(file="C:/Users/Me/Desktop/Carlos Python Projects/Day 31/images/card_back.png")

generate_word()

window.mainloop()
