from tkinter import *
from tkinter import ttk

# define some colours
blue = "#275BAD"
yellow = "#ffd311"
red = "#c92810"


def main_menu():
    """
    Creates the main menu GUI
    :return: None
    """
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
    new_game_button = Button(contents, text="New Game", height="2", width="20", command=lambda: new_game(window))
    exit_button = Button(contents, text="Exit", height="2", width="20", command=window.destroy)

    new_game_button.grid(row=0, column=0, padx=15, pady=175)
    exit_button.grid(row=0, column=1, padx=15, pady=175)

    window.mainloop()


def new_game(parent):
    """
    Creates a GUI for user to enter parameters for game
    :param parent: parent GUI
    :return: None
    """

    parent.destroy()

    # create a new window
    window = Tk()
    window.title("Wizard App")
    window.geometry("400x200")
    window['bg'] = "#275BAD"
    window.resizable(False, False)

    # display title
    title_label = Label(window, text="New Game", fg=yellow, bg=red, font=("Helvetica", 20), width=600, pady=10)
    title_label.pack()

    # spacer frame
    spacer_top = Frame(window)
    spacer_top.pack()
    spacer_label = Label(spacer_top, text="", bg=blue, height=3)
    spacer_label.pack()

    # make frame for contents
    frame = Frame(window, bg=blue)
    frame.pack()

    # create combobox
    combo_label = Label(frame, text="How many players?", bg=blue, fg='white')
    combo_label.grid(row=0)
    combo = ttk.Combobox(frame, values=["3", "4", "5", "6"], width=3)
    combo.current(0)
    combo.grid(row=0, column=1)

    # create blank label to space
    spacer2 = Label(frame, text="", bg=blue, fg=blue)
    spacer2.grid(row=1, columnspan=2)

    # create button
    ok = Button(frame, text="Ok", command=lambda: get_player_names(window, int(combo.get())), width=10)
    ok.grid(row=2, columnspan=2)

    window.mainloop()


def get_player_names(parent, players):

    num_players = players
    parent.destroy()

    window = Tk()
    window.title("Wizard App")
    window.geometry("400x300")
    window['bg'] = "#275BAD"
    window.resizable(False, False)

    # display title
    title_label = Label(window, text="Players", fg=yellow, bg=red, font=("Helvetica", 20), width=600, pady=10)
    title_label.pack()

    # spacer frame
    spacer_top = Frame(window)
    spacer_top.pack()
    spacer_label = Label(spacer_top, text="", bg=blue, height=3)
    spacer_label.pack()

    # make frame for contents
    frame = Frame(window, bg=blue)
    frame.pack()

    # display input boxes for players names to be entered
    entries = []
    if isinstance(num_players, list):
        num_players = len(num_players)
    for i in range(num_players):
        label = Label(frame, text="Player " + str(i+1), bg=blue, fg='white')
        label.grid(row=i, column=0)
        entry = Entry(frame)
        entry.grid(row=i, column=1)
        entries.append(entry)

    # create blank label to space
    spacer2 = Label(frame, text="", bg=blue, fg=blue)
    spacer2.grid(row=num_players, columnspan=2)

    # create button
    ok = Button(frame, text="Ok", width=10, command=lambda: get_names(window, [e.get() for e in entries]))
    ok.grid(row=num_players+2, columnspan=2)

    window.mainloop()


def get_names(parent, names):
    print(names)
    parent.destroy()


if __name__ == '__main__':
    main_menu()
