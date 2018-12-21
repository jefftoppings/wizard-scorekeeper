from tkinter import *
from tkinter import ttk
from game import *

# define some colours
blue = "#275BAD"
yellow = "#ffd311"
red = "#c92810"


def main_menu(parent=None):
    """
    Creates the main menu GUI
    :param parent: if there is a parent GUI
    :return: None
    """
    if parent is not None:
        parent.destroy()

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
    """
    GUI that obtains the names of players
    :param parent: parent GUI
    :param players: number of players specified in parent GUI
    :return: None
    """

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
    ok = Button(frame, text="Ok", width=10, command=lambda: initialize_game(window, [e.get() for e in entries]))
    ok.grid(row=num_players+2, columnspan=2)

    window.mainloop()


def initialize_game(parent, names):

    parent.destroy()

    window = Tk()
    window.title("Wizard App")
    window.geometry("800x600")
    window['bg'] = "#275BAD"
    window.resizable(False, False)

    # spacer frame for top
    spacer_top = Frame(window)
    spacer_top.pack()
    spacer_label = Label(spacer_top, text="", bg=blue, height=2)
    spacer_label.pack()

    # make a frame for the title
    title = Frame(window)
    title.pack()

    # place the title at the top
    title_label = Label(title, text="Scorecard", fg=yellow, bg=red, font=("Helvetica", 30), width=600, pady=30)
    title_label.pack()

    # spacer frame for middle
    spacer_mid = Frame(window)
    spacer_mid.pack()
    spacer_label = Label(spacer_mid, text="", bg=blue, height=2)
    spacer_label.pack()

    # make a frame for the contents
    contents = Frame(window, bg=blue)
    contents.pack()

    # create headings for table that will keep score
    name_label = Label(contents, text="Players/Hand#", width=12, padx=3)
    name_label.grid(row=0, column=0)
    for i in range(len(names)):
        label = Label(contents, text=names[i], width=12, padx=3)
        label.grid(row=0, column=i+1)

    # # initialize game
    # game = Game(names)
    game_over = False

    # frame for buttons at bottom
    bottom = Frame(window, bg=blue)
    bottom.pack(side=BOTTOM)

    if not game_over:
        bets = Button(bottom, text="Record Bets")
        bets.pack()
        spacer_label = Label(bottom, text="", bg=blue, height=2)
        spacer_label.pack()
    else:
        thanks = Label(bottom, text="Thanks for Playing!", font=('Helvetica', 16), bg=blue, fg='white')
        play_again = Button(bottom, text="Ok", command=lambda: main_menu(window))
        thanks.pack()
        play_again.pack()
        spacer_label = Label(bottom, text="", bg=blue, height=2)
        spacer_label.pack()

    window.mainloop()


if __name__ == '__main__':
    main_menu()
