from tkinter import *

# define some colours
blue = "#275BAD"
yellow = "#ffd311"
red = "#c92810"


def main_menu():
    window = Tk()
    window.title("Wizard App")
    window.geometry("800x600")
    window['bg'] = "#275BAD"
    window.resizable(False, False)

    # spacer frame for top
    spacer_top = Frame(window)
    spacer_top.pack()
    spacer_label = Label(spacer_top, text="", bg=blue, height=7)
    spacer_label.pack()

    # make a frame for the title
    title = Frame(window)
    title.pack()

    # make a frame for the contents
    contents = Frame(window, bg=blue)
    contents.pack()

    # place the title at the top
    title_label = Label(title, text="Wizard Scorekeeper", fg=yellow, bg=red, font=("Helvetica", 30), width=600, pady=30)
    title_label.pack()

    # put buttons at bottom
    new_game_button = Button(contents, text="New Game", height="2", width="20")
    exit_button = Button(contents, text="Exit", height="2", width="20", command=window.destroy)

    new_game_button.grid(row=0, column=0, padx=15, pady=175)
    exit_button.grid(row=0, column=1, padx=15, pady=175)

    window.mainloop()


if __name__ == '__main__':
    main_menu()
