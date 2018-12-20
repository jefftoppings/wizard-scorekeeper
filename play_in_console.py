from player import *
from game import *
from hand import *
from calculate import *

if __name__ == '__main__':
    print("*** Welcome to Wizard Scorekeeper! ***\n")

    # obtain the number of players
    valid_input = False
    num_players = 0
    while not valid_input:
        num_players = int(input("How many players will be playing? "))
        if 3 <= num_players <= 6:
            valid_input = True
        else:
            print("Wizard requires 3-6 players.")

    # obtain names of players and create list of player objects
    player_list = []
    for x in range(num_players):
        name = input("Enter Player " + str(x + 1) + "'s Name: ")
        player_list.append(Player(name))

    # initialize the game
    game = Game(player_list)
    print()
    game_over = False
    while not game_over:
        # obtain bids from everyone
        bids = []
        for player in game.players:
            bid = int(input("Enter Bid for " + player.name + ": "))
            bids.append(Hand(player, bid))

        # determine who was correct
        correct = []
        print()
        print("Input '0' for Correct, or the Number of Tricks Missed By")
        for player in game.players:
            c = int(input(player.name + ": "))
            if c == 0:
                correct.append(True)
            else:
                correct.append(c)

        # update scores
        game.update_scores(bids, correct)

        # print summary of scores
        print()
        print(game)

        # determine if game is over
        if game.current_hand >= game.number_of_hands:
            print()
            winner = None
            max_score = 0
            for player in game.players:
                if player.score > max_score:
                    max_score = player.score
                    winner = player.name
            print("The winner is", winner + "!")
            game_over = True
