from tkinter import *
from tkinter import ttk
from game import *
from player import *
from hand import *
import datetime

# define some colours
blue = "#275BAD"
yellow = "#ffd311"
red = "#c92810"
start_date = str(datetime.datetime.now())


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
    title_label = Label(window, text="Player Names", fg=yellow, bg=red, font=("Helvetica", 20), width=600, pady=10)
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
    ok = Button(frame, text="Ok", width=10, command=lambda: display_score(window, [e.get() for e in entries], None))
    ok.grid(row=num_players+2, columnspan=2)

    window.mainloop()


def display_score(parent, names, game, game_over=False):
    """
    GUI that prints out the current score for all players
    :param parent: parent GUI
    :param names: list containing names of the players, as strings
    :param game: Game object
    :param game_over: boolean stating if game has reached the final hand
    :return: None
    """

    parent.destroy()

    # create new GUI
    window = Tk()
    window.title("Wizard App")
    window.geometry("800x350")
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

    # initialize game if necessary
    if game is None:
        game = Game([Player(name) for name in names])
        # create scoresheet csv for backup
        f = open("scoresheet.txt", "w")
        f.write(start_date + '\n')
        names_all = ""
        for name in names:
            names_all += name + ","
        f.write(names_all[:-1] + '\n')
        f.close()

    # create headings for table that will keep score
    name_label = Label(contents, text="Players:", width=12, padx=3)
    name_label.grid(row=0, column=0)
    for i in range(len(names)):
        label = Label(contents, text=names[i], width=12, padx=3)
        label.grid(row=0, column=i+1)

    # put most recent score
    name_label = Label(contents, text="Score:", width=12, padx=3)
    name_label.grid(row=1, column=0)
    for i in range(len(names)):
        label2 = Label(contents, text=str(game.players[i].score), width=12, padx=3)
        label2.grid(row=1, column=i+1)

    # frame for buttons at bottom
    bottom = Frame(window, bg=blue)
    bottom.pack(side=BOTTOM)

    if not game_over:
        bets = Button(bottom, text="Record Bets", command=lambda: get_bids(window, game))
        bets.pack()
        spacer_label = Label(bottom, text="", bg=blue, height=2)
        spacer_label.pack()
    else:
        thanks = Label(bottom, text="Thanks for Playing!", font=('Helvetica', 16), bg=blue, fg='white')
        play_again = Button(bottom, text="Ok", command=lambda: main_menu(window), width=5)
        thanks.pack()
        play_again.pack()
        spacer_label = Label(bottom, text="", bg=blue, height=2)
        spacer_label.pack()

    window.mainloop()


def get_bids(parent, game):
    """
    GUI that asks for players bids to be entered
    :param parent: parent GUI
    :param game: current instance of Game Object
    :return: None
    """

    parent.destroy()

    # create new GUI
    window = Tk()
    window.title("Wizard App")
    window.geometry("400x300")
    window['bg'] = "#275BAD"
    window.resizable(False, False)

    # display title
    title_label = Label(window, text="Bids for Hand #" + str(game.current_hand), fg=yellow, bg=red, font=("Helvetica", 20),
                        width=600, pady=10)
    title_label.pack()

    # spacer frame
    spacer_top = Frame(window)
    spacer_top.pack()
    spacer_label = Label(spacer_top, text="", bg=blue, height=3)
    spacer_label.pack()

    # make frame for contents
    frame = Frame(window, bg=blue)
    frame.pack()

    # create entry boxes for bids to be entered
    bids = []
    for i in range(len(game.players)):
        label = Label(frame, text=game.players[i].name, bg=blue, fg='white')
        label.grid(row=i, column=0)
        entry = Entry(frame)
        entry.grid(row=i, column=1)
        bids.append(entry)

    # create blank label to space
    spacer2 = Label(frame, text="", bg=blue, fg=blue)
    spacer2.grid(row=len(game.players), columnspan=2)

    # create button
    ok = Button(frame, text="Ok", width=10, command=lambda: apply_bids(window, game, [b.get() for b in bids]))
    ok.grid(row=len(game.players)+2, columnspan=2)

    window.mainloop()


def apply_bids(parent, game, bids):
    """
    GUI that asks user for the number of tricks that users took
    :param parent: parent GUI
    :param game: instance of Game object
    :param bids: list of bids, represented as integers
    :return: None
    """

    parent.destroy()

    # GUI to determine who was correct
    window = Tk()
    window.title("Wizard App")
    window.geometry("400x300")
    window['bg'] = "#275BAD"
    window.resizable(False, False)

    # display title
    title_label = Label(window, text="Correctness of Bids", fg=yellow, bg=red, font=("Helvetica", 20),
                        width=600, pady=10)
    title_label.pack()

    # spacer frame
    spacer_top = Frame(window)
    spacer_top.pack()
    spacer_label = Label(spacer_top, text="", bg=blue, height=3)
    spacer_label.pack()

    # make frame for contents
    frame = Frame(window, bg=blue)
    frame.pack()

    correctness = []
    for i in range(len(game.players)):
        label = Label(frame, text=game.players[i].name + ", bid " + bids[i] + " and took: ", bg=blue, fg='white')
        label.grid(row=i, column=0)
        entry = Entry(frame)
        entry.grid(row=i, column=1)
        correctness.append(entry)

    # create blank label to space
    spacer2 = Label(frame, text="", bg=blue, fg=blue)
    spacer2.grid(row=len(game.players), columnspan=2)

    # create button
    ok = Button(frame, text="Ok", width=10, command=lambda: calculate(window, game, bids, correctness))
    ok.grid(row=len(game.players)+2, columnspan=2)

    window.mainloop()


def calculate(parent, game, bids, correctness):
    """
    Updates the scores according to bids asked for and taken by each player
    :param parent: parent GUI
    :param game: instance of Game Object
    :param bids: list of bids
    :param correctness: list containing actual number of tricks taken
    :return: None
    """

    # convert correctness and bids
    correctness = [int(c.get()) for c in correctness]
    hands = []
    for i in range(len(game.players)):
        hand = Hand(game.players[i], int(bids[i]))
        hands.append(hand)

    # determine how much each player missed by
    missed_by = []
    for i in range(len(bids)):
        missed_by.append(abs(int(bids[i])-correctness[i]))

    # apply to game
    game.update_scores(hands, missed_by)

    # update text file
    f = open("scoresheet.txt", "a+")
    scores = ""
    for player in game.players:
        scores += str(player.score) + ","
    f.write(scores[:-1] + '\n')
    f.close()

    # determine if game is over
    game_over = False
    if game.current_hand > game.number_of_hands:
        game_over = True

    display_score(parent, [x.name for x in game.players], game, game_over)


if __name__ == '__main__':
    main_menu()
